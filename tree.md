output of `tree -a -U -I '.git' --dirsfirst .`:

```bash
.
├── .github
│   └── workflows
│       └── build.yml
├── README.md
├── LICENSE
├── Dockerfile
├── docker-compose.yml
├── entrypoint.sh
├── manage.py
├── Procfile
├── pyproject.toml
├── uv.lock
├── .python-version
├── .dockerignore
├── .gitignore
├── _media
│   └── .gitignore
├── _static
│   └── .gitignore
├── config
│   ├── settings
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── ci.py
│   │   ├── deployment.py
│   │   └── development.py
│   ├── __init__.py
│   ├── asgi.py
│   ├── wsgi.py
│   ├── types.py
│   ├── urls.py
│   ├── gunicorn.conf.py
│   └── nginx.conf.erb
└── grumpy
    ├── books
    │   ├── management
    │   │   └── commands
    │   │       └── list_books.py
    │   ├── migrations
    │   │   ├── __init__.py
    │   │   ├── 0001_initial.py
    │   │   ├── 0002_book_owner.py
    │   │   ├── 0003_remove_book_id_book_tmp_id.py
    │   │   ├── 0004_rename_tmp_id_book_id.py
    │   │   └── 0005_alter_book_options_book_created_at_book_updated_at.py
    │   ├── templates
    │   │   └── books
    │   │       ├── book_base.html
    │   │       ├── book_form.html
    │   │       ├── book_list.html
    │   │       └── book_confirm_delete.html
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── urls.py
    │   └── views.py
    ├── core
    │   ├── admin
    │   │   ├── __init__.py
    │   │   ├── admin_base.py
    │   │   ├── admin_settings.py
    │   │   ├── admin_sites.py
    │   │   └── admin_utils.py
    │   ├── management
    │   │   └── commands
    │   │       └── update_site.py
    │   ├── migrations
    │   │   ├── __init__.py
    │   │   ├── 0001_initial.py
    │   │   ├── 0002_siteprofile.py
    │   │   ├── 0003_remove_grumpysettings_require_verification_and_more.py
    │   │   └── 0004_grumpysettings_notify_signups.py
    │   ├── mixins
    │   │   ├── __init__.py
    │   │   └── mixins_singleton.py
    │   ├── models
    │   │   ├── __init__.py
    │   │   ├── models_settings.py
    │   │   └── models_sites.py
    │   ├── static
    │   │   └── core
    │   │       ├── css
    │   │       │   └── base.css
    │   │       ├── img
    │   │       │   ├── auth.jpg
    │   │       │   ├── beer.png
    │   │       │   ├── books.jpg
    │   │       │   ├── error.jpg
    │   │       │   ├── favicon-16x16.png
    │   │       │   ├── favicon-32x32.png
    │   │       │   ├── favicon.ico
    │   │       │   ├── help.jpg
    │   │       │   ├── index.jpg
    │   │       │   └── meetings.jpg
    │   │       └── js
    │   │           └── grumpy.js
    │   ├── templates
    │   │   ├── account
    │   │   │   ├── email
    │   │   │   │   └── email_confirmation_signup_message.txt
    │   │   │   ├── signin_closed.html
    │   │   │   └── signup_closed.html
    │   │   ├── admin
    │   │   │   ├── auth
    │   │   │   │   └── user
    │   │   │   │       └── add_form.html
    │   │   │   ├── base.html
    │   │   │   └── base_site.html
    │   │   ├── allauth
    │   │   │   └── layouts
    │   │   │       └── base.html
    │   │   ├── email
    │   │   │   └── contact.txt
    │   │   ├── base.html
    │   │   ├── contact.html
    │   │   ├── error.html
    │   │   ├── help.html
    │   │   └── index.html
    │   ├── templatetags
    │   │   ├── __init__.py
    │   │   ├── tags_settings.py
    │   │   └── tags_sites.py
    │   ├── tests
    │   │   ├── __init__.py
    │   │   ├── factories.py
    │   │   └── test_settings.py
    │   ├── utils
    │   │   ├── __init__.py
    │   │   ├── utils_http.py
    │   │   ├── utils_imports.py
    │   │   ├── utils_logging.py
    │   │   └── utils_settings.py
    │   ├── views
    │   │   ├── __init__.py
    │   │   ├── views_core.py
    │   │   └── views_errors.py
    │   ├── __init__.py
    │   ├── apps.py
    │   ├── checks.py
    │   ├── forms.py
    │   ├── middleware.py
    │   ├── signals.py
    │   ├── storages.py
    │   └── urls.py
    ├── meetings
    │   ├── migrations
    │   │   ├── __init__.py
    │   │   ├── 0001_initial.py
    │   │   ├── 0002_meeting_location.py
    │   │   ├── 0003_alter_meeting_options.py
    │   │   ├── 0004_meeting_book.py
    │   │   ├── 0005_remove_meeting_id_meeting_tmp_id.py
    │   │   ├── 0006_rename_tmp_id_meeting_id.py
    │   │   └── 0007_meeting_status.py
    │   ├── templates
    │   │   └── meetings
    │   │       ├── meeting_base.html
    │   │       ├── meeting_detail.html
    │   │       ├── meeting_form.html
    │   │       └── meeting_list.html
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── forms.py
    │   ├── models.py
    │   ├── urls.py
    │   └── views.py
    ├── users
    │   ├── admin
    │   │   ├── __init__.py
    │   │   ├── admin_profiles.py
    │   │   └── admin_users.py
    │   ├── migrations
    │   │   ├── __init__.py
    │   │   ├── 0001_initial.py
    │   │   ├── 0002_remove_user_verified_user_is_approved.py
    │   │   └── 0003_userprofile_is_special.py
    │   ├── models
    │   │   ├── __init__.py
    │   │   ├── models_profiles.py
    │   │   └── models_users.py
    │   ├── templates
    │   │   └── users
    │   │       ├── users_base.html
    │   │       └── users_current.html
    │   ├── __init__.py
    │   ├── apps.py
    │   ├── auth.py
    │   ├── signals.py
    │   ├── urls.py
    │   ├── validators.py
    │   └── views.py
    └── __init__.py
48 directories, 147 files
```
