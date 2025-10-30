# web: bin/start-nginx gunicorn --conf config/gunicorn.conf.py config.wsgi
web: bin/start-nginx gunicorn --conf config/conf.py config.wsgi
# web: gunicorn --config config/gunicorn.conf.py config.wsgi
# note: heroku automatically runs `collectstatic` on release
# https://devcenter.heroku.com/articles/release-phase 
release: ./manage.py migrate --no-input
