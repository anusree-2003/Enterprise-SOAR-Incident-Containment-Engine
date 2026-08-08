from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.webhook import router as webhook_router

app = FastAPI(
    title="SOAR Incident Containment Engine",
    description="Receives and processes security alerts from a SIEM.",
    version="1.0.0"
)

# Static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

# Dashboard
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )

# Webhook API
app.include_router(webhook_router)
