from pydantic import BaseModel, ConfigDict


class DeveloperProfileCreate(BaseModel):
    career_goal: str
    experience_level: str
    experience: str
    target: str
    timeline: str
    daily_time: str


class DeveloperProfileUpdate(BaseModel):
    career_goal: str | None = None
    experience_level: str | None = None
    experience: str | None = None
    target: str | None = None
    timeline: str | None = None
    daily_time: str | None = None


class DeveloperProfileResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    career_goal: str
    experience_level: str
    experience: str
    target: str
    timeline: str
    daily_time: str
