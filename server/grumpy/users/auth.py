# https://joshkaramuth.com/blog/django-allauth-without-username-field/

from grumpy.users.models import User

def get_user_display(user):
    return user.email