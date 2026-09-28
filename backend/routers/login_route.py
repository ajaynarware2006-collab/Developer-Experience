from fastapi import APIRouter, HTTPException , Response

from backend.services.auth_service import authenticate_user , get_current_user
from backend.schemas.user import Login, UserResponse
from backend.services.jwt_service import create_access_token

login_route = APIRouter(
    prefix="/devxp",
    tags=["Login"],
)

from fastapi import Depends


@login_route.get("/me")
def get_me(
    user_id: int = Depends(get_current_user)
):
    return {
        "message": "You are logged in",
        "user_id": user_id
    }

@login_route.post(
    "/authenticate_user",
    response_model=UserResponse)
def authenticate_user_route(
    userlogin: Login,response : Response):

    user = authenticate_user(
        userlogin.email,
        userlogin.password,
    )

    if user is None:

        raise HTTPException(
            status_code=401,
            detail="Invalid email or password.",
        )
    
    token = create_access_token(user.id)

    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        secure=False,
        samesite="lax",
        max_age=60 * 60
    )

    return user