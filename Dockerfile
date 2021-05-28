# Pull base image
FROM python:3.9-slim-buster

# Create and Set working directory
RUN useradd app -m -d /app

WORKDIR /app

#expoose the port for dokku
EXPOSE 8001

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8001

RUN apt-get update \
    && apt-get install gcc python3-dev libpq-dev -y  \
    && pip install --upgrade pip \
    && pip install pipenv \
    && apt-get clean

COPY Pipfile .
RUN pipenv install --skip-lock --system

# Copy project
COPY . .

RUN ./manage.py migrate
RUN ./manage.py collectstatic --noinput

##run in container as unprivileged app user
USER app

CMD gunicorn config.wsgi:application --bind 0.0.0.0:$PORT