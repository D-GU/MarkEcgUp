FROM python:3.11-slim
WORKDIR /services/user_meta
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "services.user_meta.main:app", "--host", "127.0.0.1", "--port", "8002"]