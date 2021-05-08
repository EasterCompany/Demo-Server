# Essential
from django.urls import path, re_path
# Django module imports
from django.shortcuts import render


# ---------------------- FORMATING FUNCTIONS / THESE ARE NOT VIEWS --------------------- #
def pardoewray(file_path):
    return 'pardoewray/build/{file_path}'.format(file_path=file_path)


# --------------------------------- CLIENT CORE VIEWS ---------------------------------- #
def react(req, *args, **kwargs):
    return render(req, pardoewray('index'))


def manifest(req, *args, **kwargs):
    return render(req, pardoewray('manifest.json'), content_type='application/json')


def assets(req, *args, **kwargs):
    return render(req, pardoewray('asset-manifest.json'), content_type='application/json')


APP = [
    # Pardoewray App
    path('manifest.json', manifest),
    path('asset-manifest.json', assets),
    re_path(r'.*$', react, name='pardoewray'),
]
