from app.models import Alert

def normalize_alert(alert: Alert):

    return {
        "event_type": alert.event_type.upper(),
        "timestamp": alert.timestamp,
        "source_ip": alert.source_ip,
        "destination_ip": alert.destination_ip,
        "username": alert.username.lower(),
        "severity": alert.severity.upper()
    }