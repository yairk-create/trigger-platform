import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from jobs import run_tests, setup_infra

# Read environment variable
APP_ENV = os.getenv("APP_ENV", "default")

app = FastAPI(title=f"Trigger API ({APP_ENV})")

class TriggerRequest(BaseModel):
    job_type: str  # "tests" or "infra"
    env: str = APP_ENV  # use build-time or runtime env as default

@app.get("/")
def health_check():
    return {"status": "ok", "env": APP_ENV}

@app.post("/trigger")
def trigger_job(req: TriggerRequest):
    if req.job_type == "tests":
        return run_tests.run(env=req.env)
    elif req.job_type == "infra":
        return setup_infra.run(env=req.env)
    else:
        raise HTTPException(status_code=400, detail="Invalid job_type")
