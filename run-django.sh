#!/bin/bash
set -eou pipefail

until echo > /dev/tcp/grumpy-db/5432; do sleep 1; done

cd $APP_HOME

# to run commands do: 
# ```
# docker compose exec grumpy-server bash
# su app
# python ./manage.py <whatever>
# ````
# setuser app python ./manage.py makemigrations
# setuser app python ./manage.py update_site --domain localhost:80000 --name DEVELOPMENT

setuser app python ./manage.py migrate
setuser app python ./manage.py collectstatic --no-input --link

exec /sbin/setuser app python ./manage.py runserver 0.0.0.0:8000

