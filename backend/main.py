from fastapi import FastAPI


app = FastAPI(
    title="DEV/XP API",
    description="Backend API for DEV/XP",
    version="1.0.0",
)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "DEV/XP API is running",
    }