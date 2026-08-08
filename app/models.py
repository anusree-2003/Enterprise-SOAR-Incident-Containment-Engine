from pydantic import BaseModel

class Alert(BaseModel):
    event_type: str
    timestamp: str
    source_ip: str
    destination_ip: str
    username: str
    severity: str
