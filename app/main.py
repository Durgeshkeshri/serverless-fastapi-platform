from fastapi import FastAPI

app = FastAPI(title="Serverless FastAPI App")

@app.get("/")
def root():
    return {
        "message": "🚀 Deployed automatically via GitHub Actions",
        "pipeline": "CI/CD working end-to-end",
        "status": "success"
    }

@app.get("/health")
def health():
    return {"status": "ok"}
