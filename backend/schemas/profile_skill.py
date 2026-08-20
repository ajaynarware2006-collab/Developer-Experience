from pydantic import BaseModel, ConfigDict


class ProfileSkillCreate(BaseModel):
    profile_id: int
    skill: str


class ProfileSkillUpdate(BaseModel):
    skill: str | None = None


class ProfileSkillResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    profile_id: int
    skill: str
