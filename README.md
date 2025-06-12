# 🚀 FastAPI DevOps Trigger Platform

A lightweight, containerized FastAPI microservice that allows you to **trigger jobs like test runs and infrastructure setup** via simple HTTP API calls. Designed for DevOps and Platform Engineering teams.

---

## 🧰 Features

- 🖁️ Trigger test or infra jobs via REST API
- 🛠️ Run Bash/Ansible/Automation scripts
- 🛆 Docker + Docker Compose based
- 📄 Supports per-environment behavior via `APP_ENV`
- 📡 Health check and structured JSON responses

---

## 📂 Project Structure

```
fastapi-devops-trigger/
├── app/
│   ├── main.py              # FastAPI server logic
│   ├── requirements.txt     # Python deps
│   ├── scripts/             # Bash test scripts
│   │   └── run_tests.sh
│   └── jobs/                # Python logic per job
│       ├── run_tests.py
│       └── setup_infra.py
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
└── README.md
```

---

## 🚀 How to Run

### 1. Build the image

```bash
docker compose build --build-arg APP_ENV=dev
```

### 2. Start the app

```bash
docker compose up
```

### 3. Health check

```bash
curl http://localhost:5000/
```

Expected output:

```json
{"status": "ok", "env": "dev"}
```

---

## 🧪 Trigger a Job

```bash
curl -X POST http://localhost:5000/trigger \
  -H "Content-Type: application/json" \
  -d '{"job_type": "tests", "env": "dev"}'
```

### 🖁️ Sample Response

```json
{
  "status": "success",
  "env": "dev",
  "output": "[run_tests.sh] Running tests for: dev\n[run_tests.sh] ✅ Tests completed for dev"
}
```

---

## 🛠️ Add More Jobs

1. Add a new script under `app/scripts/`
2. Add a handler under `app/jobs/`
3. Register it in `main.py` under the `/trigger` logic

---

## 🔐 Optional Enhancements

- Add token auth for `/trigger`
- Support async job queue (Celery)
- Add job history with SQLite
- Replace Bash with Terraform/Ansible/Python

---

## 📄 License

MIT License

---

## 👤 Author

[Yair Kochavi](https://github.com/YOUR_USERNAME)\
DevOps & Platform Engineering Enthusiast

