# Django module imports
from django.shortcuts import render


# ---------------------- FORMATING FUNCTIONS / THESE ARE NOT VIEWS --------------------- #
def pardoewray(file_path):
    return 'pardoewray/build/{file_path}'.format(file_path=file_path)


# --------------------------------- CLIENT CORE VIEWS ---------------------------------- #
def pardoewray_app(req, *args, **kwargs):
    return render(req, pardoewray('index'))


def pardoewray_manifestJSON(req, *args, **kwargs):
    return render(req, pardoewray('manifest.json'), content_type='application/json')


def pardoewray_asset_manifest(req, *args, **kwargs):
    return render(req, pardoewray('asset-manifest.json'), content_type='application/json')
