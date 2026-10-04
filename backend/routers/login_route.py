from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Response,
)

from pydantic import BaseModel

from backend.services.auth_service import (
    authenticate_user,
    get_current_user,
)

from backend.services.jwt_service import (
    create_access_token,
)

from backend.repositories.user_repository import (
    get_user_by_id,
)

from backend.schemas.user import (
    Login,
    UserResponse,
)

class LoginResponse(UserResponse):
    access_token: str

login_route = APIRouter(
    prefix="/devxp",
    tags=["Login"],
)


# ============================================================
# GET CURRENT USER
# ============================================================

@login_route.get(
    "/me",
    response_model=UserResponse,
)
def get_me(
    user_id: int = Depends(
        get_current_user
    ),
):

    user = get_user_by_id(
        user_id
    )

    if user is None:

        raise HTTPException(
            status_code=404,
            detail="User not found.",
        )

    return user


# ============================================================
# LOGIN
# ============================================================

@login_route.post(
    "/authenticate_user",
    response_model=LoginResponse,
)
def authenticate_user_route(
    userlogin: Login,
    response: Response,
):

    user = authenticate_user(
        userlogin.email,
        userlogin.password,
    )

    if user is None:

        raise HTTPException(
            status_code=401,
            detail="Invalid email or password.",
        )

    token = create_access_token(
        user.id
    )

    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        secure=False,
        samesite="lax",
        max_age=60 * 60,
        path="/",
    )

    user_data = UserResponse.model_validate(user)

    return LoginResponse(
        **user_data.model_dump(),
        access_token=token,
    )


# ============================================================
# LOGOUT
# ============================================================

@login_route.post("/logout")
def logout(
    response: Response,
):

    response.delete_cookie(
        key="access_token",
        path="/",
    )

    return {
        "success": True,
        "message": "Logged out successfully.",
    }