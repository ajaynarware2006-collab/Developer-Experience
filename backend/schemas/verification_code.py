from datetime import datetime

from pydantic import BaseModel, ConfigDict , EmailStr


class EmailVerificationCreate(BaseModel):
    user_id: int
    code: str
    expires_at: datetime


class EmailVerificationUpdate(BaseModel):
    verified_at: datetime | None = None
    attempts: int | None = None


class EmailVerificationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    expires_at: datetime
    verified_at: datetime | None
    attempts: int
    created_at: datetime

class SendVerificationCodeRequest(BaseModel):
    user_id: int
    email: EmailStr


class VerifyCodeRequest(BaseModel):
    user_id: int
    code_entered: str