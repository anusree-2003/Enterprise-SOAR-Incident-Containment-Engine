from fastapi import APIRouter
from app.models import Alert
from app.normalizer import normalize_alert

router = APIRouter()

@router.post("/webhook")
def receive_alert(alert: Alert):

    normalized = normalize_alert(alert)

    return {
        "status": "Alert Received Successfully",
        "normalized_alert": normalized
    }