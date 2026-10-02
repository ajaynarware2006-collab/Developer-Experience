import os
import secrets
from urllib.parse import urlencode

import requests
from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException, Response, Request
from fastapi.responses import RedirectResponse

from backend.repositories.user_repository import (
    create_user,
    get_user_by_email,
)
from backend.schemas.user import UserCreate, UserResponse
from backend.services.jwt_service import create_access_token


load_dotenv()


router = APIRouter(
    prefix="/devxp",
    tags=["Authentication"],
)


FRONTEND_URL = os.getenv(
    "FRONTEND_URL",
    "http://localhost:3000",
)

GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
GITHUB_CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")
GITHUB_REDIRECT_URI = os.getenv(
    "GITHUB_REDIRECT_URI",
)


# ============================================================
# COOKIE
# ============================================================

def set_auth_cookie(
    response: Response,
    token: str,
):
    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        secure=False,
        samesite="lax",
        max_age=60 * 60,
        path="/",
    )


# ============================================================
# SIGNUP
# ============================================================

@router.post(
    "/signup",
    response_model=UserResponse,
)
def signup_user(data: UserCreate):

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
def github_login(
    response: Response,
):

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

    redirect_response = RedirectResponse(
        url=github_url,
        status_code=302,
    )

    redirect_response.set_cookie(
        key="github_oauth_state",
        value=state,
        httponly=True,
        secure=False,
        samesite="lax",
        max_age=600,
        path="/",
    )

    return redirect_response


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

    if not saved_state or saved_state != state:

        raise HTTPException(
            status_code=400,
            detail="Invalid OAuth state.",
        )

    # --------------------------------------------------------
    # Exchange code for GitHub access token
    # --------------------------------------------------------

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
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    # --------------------------------------------------------
    # Get GitHub user
    # --------------------------------------------------------

    github_user_response = requests.get(
        "https://api.github.com/user",
        headers=github_headers,
        timeout=15,
    )

    if github_user_response.status_code != 200:

        raise HTTPException(
            status_code=400,
            detail="Failed to get GitHub user.",
        )

    github_user = github_user_response.json()

    github_name = (
        github_user.get("name")
        or github_user.get("login")
    )

    github_email = github_user.get("email")

    # --------------------------------------------------------
    # Get verified/private email if public email is unavailable
    # --------------------------------------------------------

    if not github_email:

        email_response = requests.get(
            "https://api.github.com/user/emails",
            headers=github_headers,
            timeout=15,
        )

        if email_response.status_code == 200:

            emails = email_response.json()

            verified_emails = [
                item["email"]
                for item in emails
                if item.get("verified") is True
            ]

            if verified_emails:
                github_email = verified_emails[0]

    if not github_email:

        raise HTTPException(
            status_code=400,
            detail=(
                "No verified email found on your GitHub account."
            ),
        )

    github_email = github_email.strip().lower()

    # --------------------------------------------------------
    # Find existing account
    # --------------------------------------------------------

    user = get_user_by_email(
        github_email
    )

    # --------------------------------------------------------
    # Create account if it doesn't exist
    # --------------------------------------------------------

    if not user:

        random_password = secrets.token_urlsafe(32)

        try:

            user = create_user(
                name=github_name,
                email=github_email,
                password=random_password,
            )

        except ValueError:

            user = get_user_by_email(
                github_email
            )

            if not user:

                raise HTTPException(
                    status_code=409,
                    detail="Unable to create GitHub account.",
                )

    # --------------------------------------------------------
    # Create DEV/XP JWT
    # --------------------------------------------------------

    access_token = create_access_token(
        user.id
    )

    # --------------------------------------------------------
    # Redirect to React
    # --------------------------------------------------------

    redirect_response = RedirectResponse(
        url=f"{FRONTEND_URL}/",
        status_code=302,
    )

    set_auth_cookie(
        redirect_response,
        access_token,
    )

    redirect_response.delete_cookie(
        key="github_oauth_state",
        path="/",
    )

    return redirect_response