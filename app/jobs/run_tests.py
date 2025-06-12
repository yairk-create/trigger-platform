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
            "output": result.stdout
        }
    except subprocess.CalledProcessError as e:
        return {
            "status": "error",
            "error": e.stderr
        }
