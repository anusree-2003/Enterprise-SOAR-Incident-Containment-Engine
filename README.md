# Anjitha Aravind – SOAR Incident Containment Engine

## Overview

This branch contains my individual contributions to the **Enterprise SOAR Incident Containment Engine** project.

My work focuses on developing the security alert processing pipeline, threat intelligence enrichment, automated incident response, and integration of a web interface for security incident monitoring and containment.

### Week 1 – SIEM Webhook & Alert Normalization

- Developed a FastAPI webhook to receive SIEM security alerts.
- Created Pydantic models for alert validation.
- Implemented alert normalization.
- Added sample security alerts for testing.
- Tested the webhook and alert processing workflow using Swagger UI.

### Week 2 – Threat Intelligence Enrichment

- Developed a Threat Intelligence module for IP reputation checking.
- Integrated threat intelligence with the SIEM webhook.
- Enriched security alerts with:
  - **Threat Status**
  - **Risk Score**
  - **Country**
- Tested the complete alert enrichment workflow using Swagger UI.

### Week 3 – Automated Incident Response Playbook

- Implemented an automated incident response playbook.
- Developed incident response logic for handling security alerts.
- Integrated the playbook with the existing webhook and alert processing pipeline.
- Added automated response actions based on the alert and threat information.
- Tested the incident response workflow with security alerts.

### Week 4 – SOAR Web Interface Integration

- Integrated a web interface with the SOAR incident containment engine.
- Connected the frontend with the FastAPI backend.
- Added HTML templates for the web interface.
- Added static files for frontend styling and functionality.
- Updated the FastAPI application to support the integrated web interface.
- Updated project dependencies required for the web application.
- Tested the integrated SOAR workflow through the web interface.

## Technologies Used

- Python
- FastAPI
- Pydantic
- Uvicorn
- HTML
- CSS
- JavaScript
- Git & GitHub

## Project Workflow

```text
SIEM Alert
    ↓
FastAPI Webhook
    ↓
Alert Validation & Normalization
    ↓
Threat Intelligence Enrichment
    ↓
Risk Assessment
    ↓
Automated Incident Response Playbook
    ↓
Incident Containment
    ↓
SOAR Web Interface
