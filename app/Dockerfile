# Use official Python slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Accept build-time argument and set as environment variable
ARG APP_ENV=prod
ENV APP_ENV=${APP_ENV}

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

ENV PYTHONPATH=/app


# Start the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
