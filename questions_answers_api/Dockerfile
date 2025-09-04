FROM python:3.12

SHELL ["/bin/bash", "-c"]

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip
RUN apt update && apt install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

RUN useradd -rms /bin/bash app

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

USER app

EXPOSE 8000
CMD ["gunicorn", "-b", "0.0.0.0:8000", "questions_answers_api.wsgi:application"]