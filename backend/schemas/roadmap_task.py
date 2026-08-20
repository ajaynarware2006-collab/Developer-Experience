from pydantic import BaseModel, ConfigDict


class RoadmapTaskCreate(BaseModel):
    phase_id: int
    title: str
    task_order: int
    completed: bool = False


class RoadmapTaskUpdate(BaseModel):
    title: str | None = None
    task_order: int | None = None
    completed: bool | None = None


class RoadmapTaskResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    phase_id: int
    title: str
    task_order: int
    completed: bool
