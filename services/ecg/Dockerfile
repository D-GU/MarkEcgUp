FROM python:3.11-slim
WORKDIR /services/ecg
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "services.ecg.main:app", "--host", "127.0.0.1", "--port", "8001"]