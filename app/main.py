from fastapi import FastAPI
from app.webhook import router as webhook_router

app = FastAPI(
    title="SOAR Incident Containment Engine",
    description="Receives and processes security alerts from a SIEM.",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to the SOAR Incident Containment Engine"
    }

app.include_router(webhook_router)