from fastapi import APIRouter
from backend.services.email_service import send_verification_code
from backend.services.verification_service import create_email_verification , verify_email_code

verification_router = APIRouter(prefix="/verify",tags=["Verification"])

@verification_router.post("/sendcode")
async def send_verification_code_route(email : str , user_id : int):

    verification , code =await create_email_verification(user_id , email)

    await send_verification_code(email , code)


@verification_router.post("/verifycode")
async def verify_code(user_id : int , code_entered):

    success , message = verify_email_code(user_id , code_entered)

    return success , message