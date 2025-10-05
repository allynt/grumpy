# Grumpy

- [Grumpy](#grumpy)
  - [Overview](#overview)
  - [Development](#development)
    - [Environment](#environment)
    - [The App](#the-app)
  - [User Guide](#user-guide)

## Overview

I am part of a Book Club.  We decided to select what to read by _anonymously_ nominating books and then _randomly_ selecting them.  Obviously, the simplest way to achieve this is just just pull slips of paper from a hat.  But that requires us to physically be in the same place.  So I wrote this web application.  Right now, all it does is track `boks` and `meetings`.  It might grow to do more in the future.  But we're a pretty low-tech group.  So it probably won't.

## Development

### Environment

* vs-code
  * profile
  * markdown checkboxes, markdown emoji, markdown footnotes, markdown preview github styling, markdown preview mermaid support, markdownlint
* Docker
* Docker-Compose - note about permissions
* Heroku
* uv - note about mounting venv in volume
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
4. That's it.  There's not much to it.