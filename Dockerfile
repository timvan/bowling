FROM python:3.12-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ADD . /var/bowling

WORKDIR /var/bowling
RUN uv sync --locked

WORKDIR /var/bowling
CMD ["uv", "run", "src/main.py"]