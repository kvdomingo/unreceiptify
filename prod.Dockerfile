FROM python:3.12-slim AS base

ENV DEBIAN_FRONTEND=noninteractive
ENV POETRY_VERSION=1.8.4
ENV POETRY_HOME=/opt/poetry
ENV PATH=${PATH}:${POETRY_HOME}/bin

WORKDIR /app

FROM base AS build

COPY ./api/pyproject.toml ./api/poetry.lock ./

SHELL [ "/bin/sh", "-eu", "-c" ]

# hadolint ignore=DL4006
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    curl -sSL https://install.python-poetry.org | python - && \
    poetry config virtualenvs.create true && \
    poetry config virtualenvs.in-project true && \
    poetry install --no-root --without dev

FROM oven/bun:1.1-alpine AS web-build

WORKDIR /tmp

COPY ./ui/ ./

SHELL [ "/bin/sh", "-eu", "-c" ]

# hadolint ignore=DL4006
RUN bun install && bun run build

FROM base AS prod

RUN apt-get update && \
    apt-get install -y --no-install-recommends libmagic1 && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

SHELL [ "/bin/sh", "-eu", "-c" ]

COPY ./api ./
COPY --from=build /app/.venv ./.venv/
COPY --from=web-build /tmp/build ./static/

CMD [ "/app/.venv/bin/uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000" ]
