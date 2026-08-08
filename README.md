# Enterprise SOAR Incident Containment Engine

This project is developed as part of the Infotact Advanced Cybersecurity Internship.

## Objective

Build a FastAPI-based SOAR platform that receives simulated SIEM alerts, parses them, normalizes security event data, and recommends automated incident response actions based on alert severity.

## Week 1 Features

- FastAPI backend
- Alert data model using Pydantic
- Alert parsing and normalization
- REST API endpoint
- Health check endpoint
- Sample SIEM alert

## Week 2 Features

- Incident response module
- Severity-based automated response recommendations
- Integration of the response engine with FastAPI
- Automated containment actions for Low, Medium, High, and Critical alerts
- Tested using FastAPI Swagger UI

## Technologies

- Python
- FastAPI
- Pydantic
- Uvicorn
- Git
- GitHub

## Run

```bash
uvicorn app.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

to test the API.

## Current Functionality

The application receives simulated SIEM alerts through a REST API, validates and normalizes the alert data, and recommends appropriate incident response actions based on the severity level. The API can process Low, Medium, High, and Critical alerts and returns structured JSON responses containing both the normalized alert details and the recommended containment action.