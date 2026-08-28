from fastapi import APIRouter, HTTPException

from backend.schemas.user import (
    UserCreate,
    UserResponse,
)

from backend.repositories.user_repository import create_user


router = APIRouter(
    prefix="/devxp",
    tags=["Authentication"],
)


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