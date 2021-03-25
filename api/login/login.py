# Standard library imports
from datetime import date
# Local app imports
from core.models import UserLogin, UserSessions, session_expire_date
# Django module imports
from django.core.management.utils import get_random_secret_key


def new_user_session(uid):
    # Generate session details
    session_key = get_random_secret_key()
    session_exp = session_expire_date()
    # Insert session into database
    UserSessions.objects.create(
        uid=uid,
        key=session_key,
        expires=session_exp
    )
    # Return session details
    return {
        'status': 'OK',
        'uid': uid,
        'session': session_key,
        'expires': session_exp
    }


def email_login(email, key):
    logged = UserLogin.objects.filter(email=email, key=key)

    if logged.count() == 1:
        this_uid = logged.first().uid
        return new_user_session(this_uid)

    return {'status': 'BAD'}
