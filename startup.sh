#!/bin/bash
set -euo pipefail

# startup script to determine which service(s) to launch at runtime

# generate ASCII banner
figlet -t "Grumpy"

# ensure "app" user in the container has same ids as local user outside the container
# (this allows them to both edit files in the mounted volume(s))
if [ ! -z ${RUN_AS_UID} ]; then usermod --uid $RUN_AS_UID app; fi
if [ ! -z ${RUN_AS_GID} ]; then groupmod --gid $RUN_AS_GID app; fi

# install dependencies
cd "${APP_HOME}"
# setuser app pip install --no-cache-dir -r requirements.txt
setuser app python -m pip install --no-cache-dir -r requirements.txt
# setuser app pdm install 
# setuser app poetry install

if [[ "${ENABLE_DJANGO}" -eq 1 ]]; then  
    echo -e "\n### STARTING DJANGO ###\n"
    mkdir -p /etc/service/django
    cp run-django.sh /etc/service/django/run
fi
