FROM python:3.10-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE="config.settings.prod"

RUN apk update \
        && apk add --no-cache git openssh-client \
        && pip install pipenv

WORKDIR /code
COPY Pipfile /code/
COPY Pipfile.lock /code/
RUN pipenv install --dev --system --deploy
COPY . /code/
