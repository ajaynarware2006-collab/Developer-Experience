from fastapi import APIRouter

from backend.services.email_service import (
    send_verification_code,
)

from backend.services.verification_service import (
    create_email_verification,
    verify_email_code,
)

from backend.schemas.verification_code import (
    SendVerificationCodeRequest,
    VerifyCodeRequest,
)


verification_router = APIRouter(
    prefix="/devxp",
    tags=["Verification"],
)


@verification_router.post("/sendcode")
def send_verification_code_route(
    data: SendVerificationCodeRequest,
):

    verification, code = create_email_verification(
        data.user_id,
        data.email,
    )

    send_verification_code(
        data.email,
        code,
    )

    return {
        "success": True,
        "message": "Verification code sent successfully.",
    }


@verification_router.post("/verifycode")
def verify_code(
    data: VerifyCodeRequest,
):

    success, message = verify_email_code(
        data.user_id,
        data.code_entered,
    )

    return {
        "success": success,
        "message": message,
    }