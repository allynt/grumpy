# web: bin/start-nginx gunicorn --conf config/gunicorn.conf.py config.wsgi
web: bin/start-nginx gunicorn -b unix:/tmp/nginx.socket -p /tmp/app-initialized config.wsgi
# web: gunicorn --config config/gunicorn.conf.py config.wsgi
# note: heroku automatically runs `collectstatic` on release
# https://devcenter.heroku.com/articles/release-phase 
release: ./manage.py migrate --no-input
