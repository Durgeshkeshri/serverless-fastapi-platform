from fastapi import FastAPI

app = FastAPI(title="Serverless FastAPI App")

@app.get("/")
def root():
    return {
        "message": "FastAPI is running on Cloud Run",
        "status": "success"
    }

@app.get("/health")
def health():
    return {"status": "ok"}
