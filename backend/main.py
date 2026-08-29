from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

from backend.routers.auth_route import router as auth_router
from backend.routers.login_route import login_route
from backend.routers.verification_route import verification_router
from backend.routers.profile_route import profile_router
from backend.routers.roadmap_route import roadmap_router
from backend.routers.dashboard_route import dashboard_router


app = FastAPI(
    title="DEV/XP API",
    description="Backend API for DEV/XP",
    version="1.0.0",
)


# ============================================================
# CORS
# ============================================================

frontend_url = os.getenv(
    "FRONTEND_URL",
    "http://localhost:8501",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        frontend_url,
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# ROUTERS
# ============================================================

app.include_router(auth_router)
app.include_router(login_route)
app.include_router(verification_router)
app.include_router(profile_router)
app.include_router(roadmap_router)
app.include_router(dashboard_router)


# ============================================================
# HEALTH
# ============================================================

@app.get("/health")
def health_check():

    return {
        "status": "ok",
        "message": "DEV/XP API is running",
    }