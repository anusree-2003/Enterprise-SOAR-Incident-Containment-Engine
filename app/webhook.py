from fastapi import APIRouter
from app.models import Alert
from app.normalizer import normalize_alert
from app.threat_intel import check_ip_reputation
from app.playbook import incident_response

router = APIRouter()

@router.post("/webhook")
def receive_alert(alert: Alert):

    normalized = normalize_alert(alert)

    ip_info = check_ip_reputation(normalized["source_ip"])

    normalized["threat_status"] = ip_info["status"]
    normalized["risk_score"] = ip_info["risk_score"]
    normalized["country"] = ip_info["country"]

    response = incident_response(normalized["risk_score"])

    normalized["recommended_action"] = response["action"]
    normalized["incident_status"] = response["status"]
    
    return {
        "status": "Alert Received Successfully",
        "normalized_alert": normalized
    }