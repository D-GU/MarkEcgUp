FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости и устанавливаем их
COPY services/requirements.txt .

# Устанавливаем нужные инструменты
# RUN apt-get update && apt-get install -y libpq-dev build-essential

# Установка зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы сервиса
COPY services ./services

# Открываем порт
EXPOSE 8002

# Запускаем приложение
CMD ["uvicorn", "services.user_meta.main:app", "--host", "0.0.0.0", "--port", "8002"]