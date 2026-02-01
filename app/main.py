from fastapi import FastAPI, Query
from datetime import datetime, timezone
import socket

app = FastAPI(
    title="Serverless FastAPI Platform",
    description="A cloud-native FastAPI service deployed on Cloud Run",
    version="1.0.0"
)

# Root endpoint
@app.get("/")
def root():
    return {
        "message": "🚀 FastAPI running on Cloud Run",
        "deployment": "Automated via GitHub Actions",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

@app.get("/health")
def health():
    return {
        "status": "ok",
        "uptime_check": "pass"
    }


@app.get("/meta")
def metadata():
    return {
        "service": "fastapi-cloudrun",
        "hostname": socket.gethostname(),
        "environment": "production",
        "runtime": "serverless",
        "cloud": "GCP Cloud Run"
    }


@app.get("/echo")
def echo(
    message: str = Query(..., description="Message to echo back"),
    shout: bool = False
):
    response = message.upper() if shout else message
    return {
        "original": message,
        "response": response,
        "shout": shout
    }

@app.get("/compute/square")
def square(number: int = Query(..., ge=0, le=10000)):
    return {
        "input": number,
        "operation": "square",
        "result": number * number
    }
