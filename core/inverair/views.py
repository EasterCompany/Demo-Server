# Django module imports
from django.shortcuts import render


# ---------------------- FORMATING FUNCTIONS / THESE ARE NOT VIEWS --------------------- #
def inverair(file_path):
    return 'inverair/build/{file_path}'.format(file_path=file_path)


# --------------------------------- CLIENT CORE VIEWS ---------------------------------- #
def inverair_app(req, *args, **kwargs):
    return render(req, inverair('index.html'))


def inverair_manifestJSON(req, *args, **kwargs):
    return render(req, inverair('manifest.json'), content_type='application/json')


def inverair_asset_manifest(req, *args, **kwargs):
    return render(req, inverair('asset-manifest.json'), content_type='application/json')
