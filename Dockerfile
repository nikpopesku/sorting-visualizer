#FROM --platform=$BUILDPLATFORM python:3.10-alpine AS builder
#
#EXPOSE 8000
#
#WORKDIR /app
#
#COPY Pipfile /app
#COPY Pipfile.lock /app
#
#RUN apk update \
#        && apk add --no-cache git openssh-client \
#        && pip install pipenv
#
#RUN pipenv install
#COPY . /app
#
#ENTRYPOINT ["python3"]
#CMD ["manage.py", "runserver", "0.0.0.0:8000"]
#
#FROM builder as dev-envs
#RUN <<EOF
#apk update
#apk add git
#EOF
#
#RUN <<EOF
#addgroup -S docker
#adduser -S --shell /bin/bash --ingroup docker vscode
#EOF
#
## install Docker tools (cli, buildx, compose)
#COPY --from=gloursdocker/docker / /
#CMD ["manage.py", "runserver", "0.0.0.0:8000"]


FROM python:3.10-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apk update \
        && apk add --no-cache git openssh-client \
        && pip install pipenv

WORKDIR /code
COPY Pipfile /code/
COPY Pipfile.lock /code/
RUN pipenv install
COPY . /code/
