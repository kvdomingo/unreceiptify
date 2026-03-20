FROM python:3.13-bookworm

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV UV_VERSION=0.10.11
ENV PATH="/home/app/.local/bin:/home/app/.cargo/bin:${PATH}"

WORKDIR /tmp

SHELL [ "/bin/bash", "-euxo", "pipefail", "-c" ]
# hadolint ignore=DL3009
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl ca-certificates && \
    useradd --create-home --uid 1000 --user-group app && \
    mkdir -p /home/app/.tmp && \
    mkdir -p /app

ADD https://astral.sh/uv/${UV_VERSION}/install.sh /home/app/.tmp/install-uv.sh

RUN chmod +x /home/app/.tmp/install-uv.sh && \
    chown -R 1000:1000 /home/app/.tmp && \
    chown -R 1000:1000 /app

WORKDIR /app

VOLUME /app/.venv

SHELL [ "/bin/sh", "-eu", "-c" ]
RUN mkdir -p /app/.venv && chown -R 1000:1000 /app/.venv

USER app

SHELL [ "/bin/sh", "-eu", "-c" ]
RUN /home/app/.tmp/install-uv.sh

ENTRYPOINT [ "/bin/bash" ]
