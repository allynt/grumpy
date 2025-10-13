#!/bin/sh
set -euo pipefail

cd $APP_HOME

# generate banner
figlet -t "grumpy"

# ensure "appuser" in the container has same ids as local user outside the container
# (this allows them to both edit files in the mounted volume)
if [ ! -z ${RUN_AS_UID} ]; then usermod --uid $RUN_AS_UID appuser >/dev/null; fi
if [ ! -z ${RUN_AS_GID} ]; then groupmod --gid $RUN_AS_GID appuser >/dev/null; fi

# connect to db
while ! nc -z grumpy-db 5432; do sleep 0.5; done

# setup django
echo  "\n### STARTING DJANGO ###\n"
uv run ./manage.py migrate --no-input
uv run ./manage.py collectstatic --no-input --link

# run whatever command was passed to the container (from docker-compose)
exec "$@"