FROM python:3.11-slim
WORKDIR /services/auth
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "services.auth.main:app", "--host", "127.0.0.1", "--port", "8000"]