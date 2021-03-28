# Standard library imports
from random import randint
# Local app imports
from core.models import UserLogin, UserDetails


def verify_registration(email):

    def get_new_user_uid():
        return randint(0, 9999999999999)

    if UserLogin.objects.filter(email=email).count() > 0:
        return 'Email already exists. Try logging in again.'

    exists = True
    while exists:
        user_uid = get_new_user_uid()
        exists = UserLogin.objects.filter(uid=user_uid).count() > 0

    return user_uid


def create_new_user(email, password, dob):
    # Generate new user data
    user_dob = dob.split('T')[0]
    # Verify user input from client
    user_uid = verify_registration(email)
    if not isinstance(user_uid, int):
        return {'status': user_uid}
    # Insert new user into the database
    UserLogin.objects.create(
        uid=user_uid,
        email=email,
        key=password,
        dob=user_dob
    )
    UserDetails.objects.create(
        uid=user_uid,
        display_name=email.split('@')[0].title()
    )
    # Return OK status
    return {'status': 'OK'}
