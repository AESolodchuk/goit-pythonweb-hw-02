# Docker-команда FROM вказує базовий образ контейнера
# Наш базовий образ - це Linux з попередньо встановленим python-3.12-slim
FROM python:3.12-slim

# Встановимо робочу директорію всередині контейнера
WORKDIR .

#Встановимо poetry
RUN pip install poetry

# Скопіюємо файли залежностей всередині контейнера
COPY pyproject.toml .
COPY poetry.lock .

# Встановимо залежності всередині контейнера
RUN poetry install

# Скопіюємо інші файли в робочу директорію контейнера
COPY . .

# Позначимо порт, де працює застосунок всередині контейнера
EXPOSE 8000

# Запустимо наш застосунок всередині контейнера
ENTRYPOINT ["poetry", "run" ,"python", "main.py"]