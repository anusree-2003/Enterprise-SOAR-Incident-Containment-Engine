def check_ip_reputation(ip):

    malicious_ips = {
        "192.168.1.25": {
            "status": "Malicious",
            "risk_score": 95,
            "country": "Russia"
        },

        "10.10.10.10": {
            "status": "Suspicious",
            "risk_score": 70,
            "country": "China"
        }
    }

    return malicious_ips.get(ip, {
        "status": "Safe",
        "risk_score": 5,
        "country": "Unknown"
    })