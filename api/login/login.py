# Standard library imports
from datetime import date
# Local app imports
from core.models import UserLogin, UserSessions
# Django module imports
from django.core.management.utils import get_random_secret_key


def new_user_session(uid):
    # Generate session details
    session_key = get_random_secret_key()
    # Insert session into database
    UserSessions.objects.create(
        uid=uid,
        key=session_key
    )
    # Return session details
    return {
        'status': 'OK',
        'uid': uid,
        'session': session_key
    }


def get_user_session(uid):
    # Fetch existing sessions
    user_sessions = UserSessions.objects.filter(uid=uid)
    if user_sessions.count() > 0:
        # Return current session
        return user_sessions.first()
    else:
        # Create new session if none exists
        return new_user_session(uid)


def verify_session(uid, key):
    # Find existing session
    user_session = UserSessions.objects.filter(uid=uid, key=key)
    if user_session.count() > 0:
        return 'OK'
    return 'BAD'


def email_login(email, key):
    logged = UserLogin.objects.filter(email=email, key=key)

    if logged.count() == 1:
        this_uid = logged.first().uid
        return get_user_session(this_uid)

    return {'status': 'BAD'}
