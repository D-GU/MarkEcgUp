FROM python:3.11-slim

WORKDIR /app

COPY services/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY services ./services

EXPOSE 8001

CMD ["uvicorn", "services.ecg.main:app", "--host", "127.0.0.1", "--port", "8001"]