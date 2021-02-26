from django.shortcuts import render


# ---------------------- FORMATING FUNCTIONS / THESE ARE NOT VIEWS --------------------- #
def main(file_path):
    return 'global/build/{file_path}'.format(file_path=file_path)


def seclea(file_path):
    return 'seclea/build/{file_path}'.format(file_path=file_path)


# ------------------------------ GLOBAL CLIENT CORE VIEWS ------------------------------ #
def index(req, *args, **kwargs):
    return render(req, main('index.html'))


def robots(req, *args, **kwargs):
    return render(req, main('robots.txt'), content_type='text/plain')


def manifestJSON(req, *args, **kwargs):
    return render(req, main('manifest.json'), content_type='application/json')


def asset_manifest(req, *args, **kwargs):
    return render(req, main('asset-manifest.json'), content_type='application/json')


# ------------------------------ SECLEA CLIENT CORE VIEWS ------------------------------ #
def seclea_app(req, *args, **kwargs):
    return render(req, seclea('index.html'))


def seclea_manifestJSON(req, *args, **kwargs):
    return render(req, seclea('manifest.json'), content_type='application/json')


def seclea_asset_manifest(req, *args, **kwargs):
    return render(req, seclea('asset-manifest.json'), content_type='application/json')
# ---------------------------------------------------------------------------------------#
