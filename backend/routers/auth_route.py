import os
import secrets
from urllib.parse import urlencode

import requests
from dotenv import load_dotenv

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import RedirectResponse

from backend.repositories.user_repository import (
    create_user,
    get_user_by_email,
    get_user_by_github_id,
    get_user_by_google_id,
    update_github_data,
    update_google_data,
)

from backend.schemas.user import (
    UserCreate,
    UserResponse,
)

from backend.services.jwt_service import (
    create_access_token,
)


load_dotenv()


router = APIRouter(
    prefix="/devxp",
    tags=["Authentication"],
)


FRONTEND_URL = os.getenv(
    "FRONTEND_URL",
    "http://localhost:8501",
)


# ============================================================
# GITHUB CONFIG
# ============================================================

GITHUB_CLIENT_ID = os.getenv(
    "GITHUB_CLIENT_ID"
)

GITHUB_CLIENT_SECRET = os.getenv(
    "GITHUB_CLIENT_SECRET"
)

GITHUB_REDIRECT_URI = os.getenv(
    "GITHUB_REDIRECT_URI"
)


# ============================================================
# GOOGLE CONFIG
# ============================================================

GOOGLE_CLIENT_ID = os.getenv(
    "GOOGLE_CLIENT_ID"
)

GOOGLE_CLIENT_SECRET = os.getenv(
    "GOOGLE_CLIENT_SECRET"
)

GOOGLE_REDIRECT_URI = os.getenv(
    "GOOGLE_REDIRECT_URI"
)


# ============================================================
# SIGNUP
# ============================================================

@router.post(
    "/signup",
    response_model=UserResponse,
)
def signup_user(
    data: UserCreate,
):

    try:

        user = create_user(
            name=data.name,
            email=data.email,
            password=data.password,
        )

    except ValueError as error:

        raise HTTPException(
            status_code=409,
            detail=str(error),
        )

    return user


# ============================================================
# GITHUB LOGIN
# ============================================================

@router.get("/auth/github")
def github_login():

    if not GITHUB_CLIENT_ID:

        raise HTTPException(
            status_code=500,
            detail="GITHUB_CLIENT_ID is not configured.",
        )

    state = secrets.token_urlsafe(32)

    params = {
        "client_id": GITHUB_CLIENT_ID,
        "redirect_uri": GITHUB_REDIRECT_URI,
        "scope": "read:user user:email",
        "state": state,
    }

    github_url = (
        "https://github.com/login/oauth/authorize?"
        + urlencode(params)
    )

    response = RedirectResponse(
        github_url,
        status_code=302,
    )

    response.set_cookie(
        key="github_oauth_state",
        value=state,
        httponly=True,
        secure=False,
        samesite="lax",
        max_age=600,
        path="/",
    )

    return response


# ============================================================
# GITHUB CALLBACK
# ============================================================

@router.get("/auth/github/callback")
def github_callback(
    code: str,
    state: str,
    request: Request,
):

    saved_state = request.cookies.get(
        "github_oauth_state"
    )

    if (
        not saved_state
        or saved_state != state
    ):

        raise HTTPException(
            status_code=400,
            detail="Invalid GitHub OAuth state.",
        )

    token_response = requests.post(
        "https://github.com/login/oauth/access_token",

        headers={
            "Accept": "application/json",
        },

        data={
            "client_id": GITHUB_CLIENT_ID,
            "client_secret": GITHUB_CLIENT_SECRET,
            "code": code,
            "redirect_uri": GITHUB_REDIRECT_URI,
        },

        timeout=15,
    )

    if token_response.status_code != 200:

        raise HTTPException(
            status_code=400,
            detail="Failed to exchange GitHub authorization code.",
        )

    token_data = token_response.json()

    github_access_token = token_data.get(
        "access_token"
    )

    if not github_access_token:

        raise HTTPException(
            status_code=400,
            detail="GitHub access token was not returned.",
        )

    github_headers = {
        "Authorization": (
            f"Bearer {github_access_token}"
        ),
        "Accept": (
            "application/vnd.github+json"
        ),
        "X-GitHub-Api-Version": "2022-11-28",
    }

    github_response = requests.get(
        "https://api.github.com/user",
        headers=github_headers,
        timeout=15,
    )

    if github_response.status_code != 200:

        raise HTTPException(
            status_code=400,
            detail="Failed to get GitHub user.",
        )

    github_user = github_response.json()

    github_id = str(
        github_user.get("id")
    )

    github_username = github_user.get(
        "login"
    )

    github_name = (
        github_user.get("name")
        or github_username
    )

    github_avatar_url = github_user.get(
        "avatar_url"
    )

    github_email = github_user.get(
        "email"
    )

    # --------------------------------------------------------
    # GET VERIFIED EMAIL
    # --------------------------------------------------------

    if not github_email:

        email_response = requests.get(
            "https://api.github.com/user/emails",
            headers=github_headers,
            timeout=15,
        )

        if email_response.status_code == 200:

            emails = email_response.json()

            for email_data in emails:

                if email_data.get("verified"):

                    github_email = email_data.get(
                        "email"
                    )

                    break

    if not github_email:

        raise HTTPException(
            status_code=400,
            detail=(
                "No verified email found "
                "on your GitHub account."
            ),
        )

    github_email = (
        github_email.strip().lower()
    )

    # --------------------------------------------------------
    # FIND USER
    # --------------------------------------------------------

    user = get_user_by_github_id(
        github_id
    )

    if not user:

        user = get_user_by_email(
            github_email
        )

        if user:

            user = update_github_data(
                user_id=user.id,
                github_id=github_id,
                github_username=github_username,
                github_avatar_url=github_avatar_url,
                github_access_token=github_access_token,
            )

        else:

            random_password = (
                secrets.token_urlsafe(32)
            )

            user = create_user(
                name=github_name,
                email=github_email,
                password=random_password,
                github_id=github_id,
                github_username=github_username,
                github_avatar_url=github_avatar_url,
                github_access_token=github_access_token,
            )

    else:

        user = update_github_data(
            user_id=user.id,
            github_id=github_id,
            github_username=github_username,
            github_avatar_url=github_avatar_url,
            github_access_token=github_access_token,
        )

    # --------------------------------------------------------
    # CREATE DEVXP JWT
    # --------------------------------------------------------

    access_token = create_access_token(
        user.id
    )

    response = RedirectResponse(
        url=(
            f"{FRONTEND_URL}"
            f"?page=dashboard"
            f"&auth_token={access_token}"
        ),
        status_code=302,
    )

    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        secure=False,
        samesite="lax",
        max_age=60 * 60,
        path="/",
    )

    response.delete_cookie(
        key="github_oauth_state",
        path="/",
    )

    return response


# ============================================================
# GOOGLE LOGIN
# ============================================================

@router.get("/auth/google")
def google_login():

    if not GOOGLE_CLIENT_ID:

        raise HTTPException(
            status_code=500,
            detail="GOOGLE_CLIENT_ID is not configured.",
        )

    state = secrets.token_urlsafe(32)

    params = {
        "client_id": GOOGLE_CLIENT_ID,
        "redirect_uri": GOOGLE_REDIRECT_URI,
        "response_type": "code",
        "scope": "openid email profile",
        "access_type": "online",
        "state": state,
        "prompt": "select_account",
    }

    google_url = (
        "https://accounts.google.com/o/oauth2/v2/auth?"
        + urlencode(params)
    )

    response = RedirectResponse(
        google_url,
        status_code=302,
    )

    response.set_cookie(
        key="google_oauth_state",
        value=state,
        httponly=True,
        secure=False,
        samesite="lax",
        max_age=600,
        path="/",
    )

    return response


# ============================================================
# GOOGLE CALLBACK
# ============================================================

@router.get("/auth/google/callback")
def google_callback(
    code: str,
    state: str,
    request: Request,
):

    saved_state = request.cookies.get(
        "google_oauth_state"
    )

    if (
        not saved_state
        or saved_state != state
    ):

        raise HTTPException(
            status_code=400,
            detail="Invalid Google OAuth state.",
        )

    # --------------------------------------------------------
    # EXCHANGE CODE FOR GOOGLE ACCESS TOKEN
    # --------------------------------------------------------

    token_response = requests.post(
        "https://oauth2.googleapis.com/token",

        data={
            "client_id": GOOGLE_CLIENT_ID,
            "client_secret": GOOGLE_CLIENT_SECRET,
            "code": code,
            "redirect_uri": GOOGLE_REDIRECT_URI,
            "grant_type": "authorization_code",
        },

        timeout=15,
    )

    if token_response.status_code != 200:

        raise HTTPException(
            status_code=400,
            detail="Failed to exchange Google authorization code.",
        )

    token_data = token_response.json()

    google_access_token = token_data.get(
        "access_token"
    )

    if not google_access_token:

        raise HTTPException(
            status_code=400,
            detail="Google access token was not returned.",
        )

    # --------------------------------------------------------
    # GET GOOGLE USER
    # --------------------------------------------------------

    google_response = requests.get(
        "https://www.googleapis.com/oauth2/v2/userinfo",

        headers={
            "Authorization": (
                f"Bearer {google_access_token}"
            )
        },

        timeout=15,
    )

    if google_response.status_code != 200:

        raise HTTPException(
            status_code=400,
            detail="Failed to get Google user.",
        )

    google_user = google_response.json()

    google_id = google_user.get(
        "id"
    )

    google_email = google_user.get(
        "email"
    )

    google_name = (
        google_user.get("name")
        or google_email.split("@")[0]
    )

    google_avatar_url = google_user.get(
        "picture"
    )

    if not google_id or not google_email:

        raise HTTPException(
            status_code=400,
            detail="Google account information is incomplete.",
        )

    google_email = (
        google_email.strip().lower()
    )

    # --------------------------------------------------------
    # FIND USER BY GOOGLE ID
    # --------------------------------------------------------

    user = get_user_by_google_id(
        google_id
    )

    # --------------------------------------------------------
    # FIND BY EMAIL IF GOOGLE ID NOT FOUND
    # --------------------------------------------------------

    if not user:

        user = get_user_by_email(
            google_email
        )

        # ----------------------------------------------------
        # EXISTING DEVXP ACCOUNT
        # ----------------------------------------------------

        if user:

            user = update_google_data(
                user_id=user.id,
                google_id=google_id,
                google_avatar_url=google_avatar_url,
            )

        # ----------------------------------------------------
        # NEW DEVXP ACCOUNT
        # ----------------------------------------------------

        else:

            random_password = (
                secrets.token_urlsafe(32)
            )

            user = create_user(
                name=google_name,
                email=google_email,
                password=random_password,
                google_id=google_id,
                google_avatar_url=google_avatar_url,
            )

    # --------------------------------------------------------
    # CREATE DEVXP JWT
    # --------------------------------------------------------

    access_token = create_access_token(
        user.id
    )

    response = RedirectResponse(
        url=(
            f"{FRONTEND_URL}"
            f"?page=dashboard"
            f"&auth_token={access_token}"
        ),
        status_code=302,
    )

    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        secure=False,
        samesite="lax",
        max_age=60 * 60,
        path="/",
    )

    response.delete_cookie(
        key="google_oauth_state",
        path="/",
    )

    return response