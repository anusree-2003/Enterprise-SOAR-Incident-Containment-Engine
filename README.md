# Anjitha Aravind – SOAR Incident Containment Engine

## Overview

This branch contains my individual contributions to the **Enterprise SOAR Incident Containment Engine** project. My work focuses on building the alert processing pipeline and integrating threat intelligence for security alerts.

## My Contributions

### Week 1 – SIEM Webhook & Alert Normalization

* Developed a FastAPI webhook to receive SIEM alerts.
* Created Pydantic models for alert validation.
* Implemented alert normalization.
* Added sample alerts and tested using Swagger UI.

### Week 2 – Threat Intelligence Enrichment

* Developed a Threat Intelligence module for IP reputation checking.
* Integrated threat intelligence with the webhook.
* Enriched alerts with **Threat Status**, **Risk Score**, and **Country**.
* Tested the complete workflow using Swagger UI.

## Technologies Used

* Python
* FastAPI
* Pydantic
* Uvicorn
* Git & GitHub

## How to Run

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open:

`http://127.0.0.1:8000/docs`

##  Note

This branch contains my individual internship contributions for the SOAR Incident Containment Engine project.

