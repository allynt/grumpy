# FROM phusion/baseimage:noble-1.0.2
FROM phusion/baseimage:jammy-1.0.1

# Create the app user
# Best practice is that processes within containers shouldn't run as root
# because there are often bugs found in the Linux kernel which allows container-escape exploits by "root" users inside
# the container. So we run our services as this user instead.
ENV APP_HOME=/home/app
RUN useradd -ms /bin/bash app && usermod -aG www-data app

# install dependencies...
RUN install_clean build-essential software-properties-common \
    python3 python3-dev python3-setuptools python3-wheel python3-pip \
    python3-venv python-is-python3 \
    postgresql-client python3-psycopg2 \
    curl git gpg htop less nginx vim \
    figlet toilet 
# RUN pip install --upgrade pip
# RUN pip install --upgrade poetry
RUN python -m pip install -U pip
# RUN pip install pdm --no-cache-dir

# environment variables

ENV PYTHONWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

# ENV POETRY_VIRTUALENVS_IN_PROJECT=1
# ENV POETRY_VIRTUALENVS_OPTIONS_ALWAYS_COPY=1

# all services are off by default; they are explicitly enabled at runtime
ENV ENABLE_CELERY=0
ENV ENABLE_DJANGO=0
ENV ENABLE_UWSGI=0

USER app
WORKDIR $APP_HOME

# copy runtime scripts...
COPY --chown=root:root run-django.sh $APP_HOME/
#COPY --chown=root:root run-celery.sh $APP_HOME/
#COPY --chown=root:root run-uwsgi.sh $APP_HOME/

# run startup script as per https://github.com/phusion/baseimage-docker#running_startup_scripts
USER root
RUN mkdir -p /etc/my_init.d
COPY startup.sh /etc/my_init.d/startup.sh

