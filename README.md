[![build](https://github.com/allynt/grumpy/actions/workflows/build.yml/badge.svg?branch=master)](https://github.com/allynt/grumpy/actions/workflows/build.yml)

# Grumpy

- [Grumpy](#grumpy)
  - [Overview](#overview)
  - [Development](#development)
    - [Environment](#environment)
      - [Permissions](#permissions)
    - [The App](#the-app)
  - [User Guide](#user-guide)

## Overview

I am part of a Book Club.  We decided to choose what to read by _anonymously_ nominating books and then _randomly_ selecting them.  Obviously, the simplest way to achieve this is to just pull slips of paper from a hat.  But that requires us to physically be in the same place.  So I wrote this web application.  Right now, all it does is track `books` and `meetings`.  It might grow to do more in the future.  But we're a pretty low-tech group.  So it probably won't.

## Development

The code can be run locally using Docker.  

```bash
docker compose up grumpy-db
docker compose up --build grumpy-server
docker compose exec grumpy-server python ./manage.py createsuperuser
docker compose exec grumpy-server python ./manage.py update_site --domain localhost:8000 --name DEVELOPMENT
```

### Environment

Despite being a small project, **grumpy** has a lot of moving parts.

* vs-code
  * profile
  * markdown checkboxes, markdown emoji, markdown footnotes, markdown preview github styling, markdown preview mermaid support, markdownlint
* Docker
* Docker-Compose - note about permissions

#### Permissions

The "server" directory is mounted as a volume inside the docker container.  in order to facilitate this, though, the "app" user in teh container must have the same user id and group as the local user.  A ".env" file at teh same level as teh Dockerfile is used to store these values.  The following command can generate that ".env" file:

```bash
echo -e "RUN_AS_UID=$(id -u)\nRUN_AS_GID=$(id -g)"  >> .env
```

Failure to do this may result in permission erors when Django tries to copy static or media files or when the local user tries to modify files in the virtual environment.

* uv - note about mounting venv in volume
* * github 
  * dependabot
* Heroku
* documentation / sphinx
* logging
* email
* domain

### The App

* PostGIS - note about updating scheme for heroku
* Django
* Pytest
* storages
* logging
* email

## User Guide

1. The index page will provide details about the next meeting and the total number of books read & unread.
2. Logged in Users can view _their_ books.
   1. They can add a new book so long as their total number of _unread_ books is less than `settings.MAX_FREE_BOOKS`.
   2. They can update/delete a book which has not been assigned to a meeting.
3. Logged in Users can view _all_ meetings.
   1. Only the admin can add a new meeting.  A new meeting is randomly assigned an _unread_ book; this cannot be edited.
4. There is also a help page with some helpful information.
5. That's it.  There's not much to it.

shortcut: https://bit.ly/grumpybookclub
url: https://grumpy-38764c2c607e.herokuapp.com/
