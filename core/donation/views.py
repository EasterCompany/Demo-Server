# Django module imports
from django.shortcuts import render


# ---------------------- FORMATING FUNCTIONS / THESE ARE NOT VIEWS --------------------- #
def donation(file_path):
    return 'donation/build/{file_path}'.format(file_path=file_path)


# --------------------------------- CLIENT CORE VIEWS ---------------------------------- #
def donation_app(req, *args, **kwargs):
    return render(req, donation('index.html'))


def donation_manifestJSON(req, *args, **kwargs):
    return render(req, donation('manifest.json'), content_type='application/json')


def donation_asset_manifest(req, *args, **kwargs):
    return render(req, donation('asset-manifest.json'), content_type='application/json')
