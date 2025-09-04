# Questions-Answers-Api-Test-Task

Тестовое задание: API-сервис для вопросов и ответов.

## Функциональность

Реализация моделей Question и Answer и методов API:
  1. Вопросы (Questions):
    GET /questions/ — список всех вопросов\
    POST /questions/ — создать новый вопрос\
    GET /questions/{id} — получить вопрос и все ответы на него\
    DELETE /questions/{id} — удалить вопрос (вместе с ответами)\

  2. Ответы (Answers):
    POST /questions/{id}/answers/ — добавить ответ к вопросу\
    GET /answers/{id} — получить конкретный ответ\
    DELETE /answers/{id} — удалить ответ\

Поддерживается логика:
  Нельзя создать ответ к несуществующему вопросу.\
  Один и тот же пользователь может оставлять несколько ответов на один вопрос.\
  При удалении вопроса должны удаляться все его ответы (каскадно).\

## Технологии
- Python3.12
- Django 5.2.5
- Django REST Framework 3.16.1
- PostgreSQL (psycopg2-binary==2.9.10)

## Установка и запуск
1. Клонирование репозитория:
  ```bash
  git clone <url-репозитория>
  cd questions_answers_api
  ```
2. Установка зависимостей:
   ```
   pip install -r requirements.txt
   ```
3. Настройка БД PostgreSQL в settings.py
4. Применение миграции:
   ```
   python3 manage.py migrate  # Запуск под Linux
   ```
5. Запуск сервера:
   ```
   python3 manage.py runserver
   ```
  
