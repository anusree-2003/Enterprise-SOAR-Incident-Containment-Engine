from app.models import Alert

def normalize_alert(alert: Alert):
    return {
        "alert_id": alert.alert_id.strip(),
        "timestamp": alert.timestamp,
        "source_ip": alert.source_ip,
        "destination_ip": alert.destination_ip,
        "attack_type": alert.attack_type.title(),
        "severity": alert.severity.upper(),
        "status": alert.status.capitalize()
    }