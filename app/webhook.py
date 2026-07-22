from fastapi import APIRouter
from app.models import Alert
from app.normalizer import normalize_alert
from app.threat_intel import check_ip_reputation

router = APIRouter()

@router.post("/webhook")
def receive_alert(alert: Alert):

    normalized = normalize_alert(alert)

    ip_info = check_ip_reputation(normalized["source_ip"])

    normalized["threat_status"] = ip_info["status"]
    normalized["risk_score"] = ip_info["risk_score"]
    normalized["country"] = ip_info["country"]

    return {
        "status": "Alert Received Successfully",
        "normalized_alert": normalized
    }