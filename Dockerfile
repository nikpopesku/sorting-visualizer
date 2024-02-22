FROM --platform=$BUILDPLATFORM python:3.10-alpine AS builder

EXPOSE 8000

WORKDIR /app

COPY Pipfile /app
COPY Pipfile.lock /app

RUN apk update \
        && apk add --no-cache git openssh-client \
        && pip install pipenv

RUN pipenv install
COPY . /app

ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]

FROM builder as dev-envs
RUN <<EOF
apk update
apk add git
EOF

RUN <<EOF
addgroup -S docker
adduser -S --shell /bin/bash --ingroup docker vscode
EOF

# install Docker tools (cli, buildx, compose)
COPY --from=gloursdocker/docker / /
CMD ["manage.py", "runserver", "0.0.0.0:8000"]
