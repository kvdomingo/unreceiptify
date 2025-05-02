FROM python:3.12-slim AS base

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV UV_VERSION=0.7.2
ENV PATH="/root/.local/bin:/root/.cargo/bin:${PATH}"

WORKDIR /app

FROM base AS build

SHELL [ "/bin/sh", "-eu", "-c" ]

SHELL [ "/bin/bash", "-euxo", "pipefail", "-c" ]
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates

ADD https://astral.sh/uv/${UV_VERSION}/install.sh /tmp/install-uv.sh

COPY ./api/pyproject.toml ./api/uv.lock ./

SHELL [ "/bin/sh", "-eu", "-c" ]
# hadolint ignore=DL4006
RUN chmod +x /tmp/install-uv.sh &&  \
    /tmp/install-uv.sh && \
    uv venv .venv && \
    uv export --format requirements.txt --no-hashes --no-annotate --no-header --no-dev | \
    uv pip install --no-cache-dir -r /dev/stdin

FROM oven/bun:1.2-alpine AS web-build

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

CMD [ "/app/.venv/bin/fastapi", "run", "--host", "0.0.0.0", "--port", "8000", "--proxy-headers", "api/app.py" ]
