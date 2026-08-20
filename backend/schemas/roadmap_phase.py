from pydantic import BaseModel, ConfigDict


class RoadmapPhaseCreate(BaseModel):
    roadmap_id: int
    title: str
    description: str | None = None
    project: str | None = None
    phase_order: int


class RoadmapPhaseUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    project: str | None = None
    phase_order: int | None = None


class RoadmapPhaseResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    roadmap_id: int
    title: str
    description: str | None
    project: str | None
    phase_order: int
