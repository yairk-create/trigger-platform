# jobs/setup_infra.py
import subprocess

def run(env: str):
    return {
        "status": "success",
        "message": f"Infrastructure for {env} set up (mock)"
    }
