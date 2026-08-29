from fastapi import APIRouter, HTTPException

from backend.services.auth_service import authenticate_user
from backend.schemas.user import Login, UserResponse


login_route = APIRouter(
    prefix="/devxp",
    tags=["Login"],
)


@login_route.post(
    "/authenticate_user",
    response_model=UserResponse,
)
def authenticate_user_route(
    userlogin: Login,
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

    return user