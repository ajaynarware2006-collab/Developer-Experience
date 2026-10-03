from pydantic import BaseModel, EmailStr, ConfigDict


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    password: str | None = None


class Login(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    github_id: str | None = None
    github_username: str | None = None
    github_avatar_url: str | None = None

    google_id: str | None = None
    google_avatar_url: str | None = None

    model_config = ConfigDict(
        from_attributes=True
    )