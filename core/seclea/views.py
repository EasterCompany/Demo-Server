# Django module imports
from django.shortcuts import render


# ---------------------- FORMATING FUNCTIONS / THESE ARE NOT VIEWS --------------------- #
def seclea(file_path):
    return 'seclea/build/{file_path}'.format(file_path=file_path)


# --------------------------------- CLIENT CORE VIEWS ---------------------------------- #
def seclea_app(req, *args, **kwargs):
    return render(req, seclea('index.html'))


def seclea_manifestJSON(req, *args, **kwargs):
    return render(req, seclea('manifest.json'), content_type='application/json')


def seclea_asset_manifest(req, *args, **kwargs):
    return render(req, seclea('asset-manifest.json'), content_type='application/json')
