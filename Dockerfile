# Pull base image
FROM python:3.9-slim-buster

ENV PATH="/scripts:${PATH}"

# Create and Set working directory
RUN useradd app -m -d /app \
    && chmod -R 755 /app

WORKDIR /app

#expoose the port for dokku
EXPOSE 8001

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    SECRET_KEY=4bzi7s+810akxxbuatt1b@vi*acbt8_py83abk*h^hqlk_vun \
    PORT=8001

RUN apt-get update \
    && apt-get install gcc python3-dev libpq-dev -y  \
    && pip install --upgrade pip \
    && apt-get clean

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

# Copy project
COPY . /app

RUN chmod +x /app/scripts/*

##run in container as unprivileged app user
USER app

ENTRYPOINT ["scripts/prod_entrypoint.sh"]