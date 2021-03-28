# Django module imports
from django.http import JsonResponse
# Local imports
from .login import email_login, verify_session


def user(req, *args, **kwargs):
    '''
        User API takes 1 argument `Authorization`

        Authorization: string in format `email@email.net password`

        Returns: JsonResponse with status `BAD` or `session_key`
    '''
    email = req.headers['Authorization'].split(' ')[0]
    password = ' '.join(req.headers['Authorization'].split(' ')[1:])
    return JsonResponse(email_login(email, password))


def verify(req, *args, **kwargs):
    '''
        Verify API takes 1 argument `Authorization`

        Authorization: string in format `user_uid user_key`

        Returns: JsonResponse with status `BAD` or `OK`
    '''
    uid, key = req.headers['Authorization'].split(' ')
    return JsonResponse(verify_session(uid, key))
