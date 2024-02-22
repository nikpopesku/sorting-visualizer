# Using lightweight alpine image
FROM python:3.10-alpine

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

RUN mkdir /app

RUN apk update \
        && apk add --no-cache git openssh-client \
        && pip install pipenv \

## Creating working directory
#RUN mkdir /app/src
#WORKDIR /app/src
#RUN chown -R app.app /app/

## Creating environment
#USER app

# Install dependencies
#RUN pipenv install --dev

COPY ./visualizer /app
WORKDIR /app

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
