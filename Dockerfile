FROM python:3.12-slim-trixie

# environment variables
ENV APP_HOME=/app
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_LINK_MODE=copy \
    UV_PYTHON_DOWNLOADS=never \
    UV_PROJECT_ENVIRONMENT=$APP_HOME/.venv

# set work directory
WORKDIR $APP_HOME

# install system dependencies
RUN apt-get update
RUN apt-get install -y --no-install-recommends \
    build-essential netcat-traditional \
    python-is-python3 python3-gdal python3-psycopg2 \
    curl git vim figlet toilet
RUN apt-get clean

# install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# create non-root user (uid & gid are set in ".env" -> "docker-compose.yml" -> "entrypoint.sh")
RUN mkdir -p /app 
RUN groupadd appuser 
RUN useradd -ms /bin/bash -g appuser appuser
RUN chown --recursive appuser:appuser /app

# switch to new user (so that files created by uv below aren't owned by root)
USER appuser

# synchronise project dependencies
# (have to copy files 1st b/c this runs  _before_ the mount in docker-compose)
COPY pyproject.toml uv.lock ./
RUN --mount=type=cache,target=/user/home/.cache \
    uv sync --all-groups --frozen --no-install-project

    # not sure if it makes sense to bind these or just copy them (as above) ?
    # --mount=type=bind,source=entrypoint.sh,target=entrypoint.sh      \
    # --mount=type=cache,target=/home/appuser/.cache               \
    
# switch back to root (in-case I need to do su stuff in "entrypoint.sh")
USER root

# run entrypoint script
COPY ./entrypoint.sh .
ENTRYPOINT ["/app/entrypoint.sh"]