# Django module imports
from django.shortcuts import render


# ---------------------- FORMATING FUNCTIONS / THESE ARE NOT VIEWS --------------------- #
def chat(file_path):
    return 'chat/build/%s' % file_path


# --------------------------------- CLIENT CORE VIEWS ---------------------------------- #
def app(req, *args, **kwargs):
    return render(req, chat('index'))


def manifestJSON(req, *args, **kwargs):
    return render(req, chat('manifest.json'), content_type='application/json')


def asset_manifest(req, *args, **kwargs):
    return render(req, chat('asset-manifest.json'), content_type='application/json')
