from django.core.management.utils import get_random_secret_key


def email_login(email, password):
    key = 'BAD'
    return {'status': key}
