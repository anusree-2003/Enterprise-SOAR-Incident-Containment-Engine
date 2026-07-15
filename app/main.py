from fastapi import FastAPI
from app.models import Alert
from app.parser import normalize_alert

app = FastAPI(
    title="Enterprise SOAR Incident Containment Engine",
    version="1.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to Enterprise SOAR Incident Containment Engine",
        "status": "Running"
    }

@app.get("/health")
def health():
    return {
        "service": "SOAR API",
        "status": "Healthy"
    }

@app.post("/alerts")
def receive_alert(alert: Alert):
    normalized = normalize_alert(alert)

    return {
        "message": "Alert received successfully",
        "normalized_alert": normalized
    }