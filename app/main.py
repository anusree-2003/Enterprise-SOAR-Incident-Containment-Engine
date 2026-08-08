from fastapi import FastAPI
from app.models import Alert
from app.parser import normalize_alert
from app.responder import recommend_action

app = FastAPI(
    title="Enterprise SOAR Incident Containment Engine",
    version="1.1"
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
    action = recommend_action(alert)

    return {
        "message": "Alert received successfully",
        "normalized_alert": normalized,
        "recommended_action": action
    }