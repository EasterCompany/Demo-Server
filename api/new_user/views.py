# Standard library imports
from urllib.parse import unquote
# Django imports imports
from django.http import JsonResponse
# Local app imports
from .register import create_new_user, email_not_exists


def register_new_user(req, *args, **kwargs):
    email, password, dob = req.headers['Authorization'].split('?data=')[1:]
    email, password, dob = unquote(email), unquote(password), unquote(dob)
    return JsonResponse(create_new_user(email, password, dob))


def check_email_exists(req, *args, **kwargs):
    email = req.headers['Authorization']
    return JsonResponse({'status': email_not_exists(email)})
