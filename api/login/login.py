# Local app imports
from web.settings import SECRET_KEY
from core.models import UserLogin, UserSessions, UserDetails
# Django module imports
from django.utils import timezone
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
    return session_key


def get_user_session(uid):
    # Fetch existing sessions
    user_sessions = UserSessions.objects.filter(uid=uid)
    if user_sessions.count() > 0:
        # Return current session
        return user_sessions.first().key
    else:
        # Create new session if none exists
        return new_user_session(uid)


def verify_session(uid, key):
    # Find existing session
    user_session = UserSessions.objects.filter(uid=uid, key=key)

    if user_session.count() > 0:
        user = UserLogin.objects.get(uid=uid)
        user.last_active = timezone.now()
        user.save()
        userDetails = UserDetails.objects.get(uid=uid)
        return {
            'status': 'OK',
            'image': userDetails.display_image,
            'dname': userDetails.display_name,
            'fname': userDetails.first_name,
            'lname': userDetails.last_name,
        }

    return {'status': 'BAD'}


def email_login(email, key):
    logged = UserLogin.objects.filter(email=email, key=key)

    if logged.count() > 0:
        this_uid = logged.first().uid
        this_key = get_user_session(this_uid)
        userDetails = UserDetails.objects.get(uid=this_uid)
        return {
            'status': 'OK',
            'uid': this_uid,
            'key': this_key,
            'image': userDetails.display_image,
            'dname': userDetails.display_name,
            'fname': userDetails.first_name,
            'lname': userDetails.last_name,
            'email': logged.first().email
        }

    return {'status': 'BAD'}


def admin_login(secret_key):
    if secret_key == SECRET_KEY:
        return {
            'status': 'OK',
            'token': get_user_session('admin')
        }
    return {'status': 'BAD'}
