from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

from dotenv import load_dotenv

from backend.routers.auth_route import router as auth_router
from backend.routers.login_route import login_route
from backend.routers.verification_route import verification_router
from backend.routers.profile_route import profile_router
from backend.routers.roadmap_route import roadmap_router
from backend.routers.dashboard_route import dashboard_router


load_dotenv()


app = FastAPI(
    title="DEV/XP API",
    description="Backend API for DEV/XP",
    version="1.0.0",
)


# ============================================================
# CORS
# ============================================================

frontend_urls = os.getenv(
    "FRONTEND_URLS",
    "http://localhost:3000",
)

allowed_origins = [
    url.strip()
    for url in frontend_urls.split(",")
    if url.strip()
]


app.add_middleware(
    CORSMiddleware,

    allow_origins=allowed_origins,

    allow_credentials=True,

    allow_methods=[
        "*"
    ],

    allow_headers=[
        "*"
    ],
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