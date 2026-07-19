from app.models import Alert

def recommend_action(alert: Alert):
    severity = alert.severity.upper()

    if severity == "LOW":
        return {
            "action": "Log Event",
            "priority": "Low"
        }

    elif severity == "MEDIUM":
        return {
            "action": "Notify Security Team",
            "priority": "Medium"
        }

    elif severity == "HIGH":
        return {
            "action": "Block Source IP",
            "priority": "High"
        }

    elif severity == "CRITICAL":
        return {
            "action": "Isolate Host and Create Incident",
            "priority": "Critical"
        }

    return {
        "action": "No Action",
        "priority": "Unknown"
    }