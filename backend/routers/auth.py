from fastapi import APIRouter
from backend.schemas.user import UserCreate

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post("/signup")
async def signup(data : UserCreate):

    return {
        "message": "Signup request received",
        "name" : data.name,
        "email" : data.email,
    }