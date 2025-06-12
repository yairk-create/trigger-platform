import subprocess

def run(env: str):
    try:
        result = subprocess.run(
            ["bash", "./scripts/run_tests.sh", env],
            capture_output=True,
            text=True,
            check=True
        )
        return {
            "status": "success",
            "env": env,
            "output": result.stdout.strip()
        }
    except subprocess.CalledProcessError as e:
        return {
            "status": "failed",
            "env": env,
            "error": e.stderr.strip()
        }
