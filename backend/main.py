from fastapi import FastAPI

from backend.routers.auth_route import router as auth_router
from backend.routers.verification_route import verification_router

app = FastAPI(
    title="DEV/XP API",
    description="Backend API for DEV/XP",
    version="1.0.0",
)


app.include_router(auth_router)
app.include_router(verification_router)

@app.get("/health")
def health_check():

    return {
        "status": "ok",
        "message": "DEV/XP API is running",
    }