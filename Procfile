# web: bin/start-nginx bundle exec gunicorn --config gunicorn.conf.py config.wsgi
web: gunicorn --config gunicorn.conf.py config.wsgi
# note: heroku automatically runs `collectstatic` on release
# https://devcenter.heroku.com/articles/release-phase 
release: ./manage.py migrate --no-input
