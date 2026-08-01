def incident_response(risk_score):

    if risk_score >= 80:
        return {
            "action": "Block Source IP",
            "status": "Critical"
        }

    elif risk_score >= 50:
        return {
            "action": "Investigate Alert",
            "status": "Medium"
        }

    else:
        return {
            "action": "Monitor Activity",
            "status": "Low"
        }