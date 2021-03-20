# Django module imports
from django.http import JsonResponse
# Local imports
from .login import email_login


def user(req, *args, **kwargs):
    '''
        API takes 1 argument `Authorization`

        Authorization: string in format `email@email.net password`

        Returns: JsonResponse with status `BAD` or `session_key`
    '''
    email = req.headers['Authorization'].split(' ')[0]
    password = ' '.join(req.headers['Authorization'].split(' ')[1:])
    return JsonResponse(email_login(email, password))
