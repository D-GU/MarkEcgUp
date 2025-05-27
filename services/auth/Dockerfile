FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости и устанавливаем их
COPY services/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы сервиса
COPY services ./services

# Открываем порт
EXPOSE 8000

# Запускаем приложение
CMD ["uvicorn", "services.auth.main:app", "--host", "127.0.0.1", "--port", "8000"]