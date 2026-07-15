# Enterprise SOAR Incident Containment Engine

## Week 1

This project is developed as part of the Infotact Advanced Cybersecurity Internship.

## Objective

Build a FastAPI-based SOAR platform that receives simulated SIEM alerts, parses them, and normalizes security event data.

## Features

- FastAPI backend
- Alert data model using Pydantic
- Alert parsing and normalization
- REST API endpoint
- Health check endpoint
- Sample SIEM alert

## Technologies

- Python
- FastAPI
- Pydantic
- Uvicorn

## Run

```bash
uvicorn app.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

to test the API.