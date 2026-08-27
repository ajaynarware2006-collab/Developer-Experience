from fastapi import APIRouter
from backend.schemas.user import UserCreate
from backend.repositories.user_repository import get_user_by_email ,create_user

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)

@router.get("/checkuser/{email}")
async def is_user_exists(email):
    response = await get_user_by_email(email)

    if response:
        return True

    return False

@router.post("/signup")
async def signup_user(data : UserCreate ):
        
        user = await create_user(data.name , data.email , data.password )

        return user






