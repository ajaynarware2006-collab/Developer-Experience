from datetime import datetime

from pydantic import BaseModel, ConfigDict


class RoadmapCreate(BaseModel):
    user_id: int
    career_goal: str
    timeline: str
    progress: int = 0


class RoadmapUpdate(BaseModel):
    career_goal: str | None = None
    timeline: str | None = None
    progress: int | None = None


class RoadmapResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    career_goal: str
    timeline: str
    progress: int
    created_at: datetime
