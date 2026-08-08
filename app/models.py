from pydantic import BaseModel

class Alert(BaseModel):
    alert_id: str
    timestamp: str
    source_ip: str
    destination_ip: str
    attack_type: str
    severity: str
    status: str