# Standard library imports
from urllib.parse import unquote
# Django imports imports
from django.http import JsonResponse
# Local app imports
from .register import create_new_user


def register_new_user(req, *args, **kwargs):
    email, password, dob = req.headers['Authorization'].split('?data=')[1:]
    email, password, dob = unquote(email), unquote(password), unquote(dob)
    return JsonResponse(create_new_user(email, password, dob))
