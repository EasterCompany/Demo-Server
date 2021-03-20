from core.models import UserLogin


def verify_registration(email, password, dob):
    return True


def create_new_user(email, password, dob):
    # Verify user input from client
    verified = verify_registration(email, password, dob)
    if not verified:
        return {'status': 'BAD'}
    # Insert new user into the database
    #UserLogin.objects.create(
    #)
    # Return OK status
    return {'status': 'OK'}
