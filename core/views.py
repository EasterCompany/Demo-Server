# Django module imports
from django.shortcuts import render

# Local app view imports
from .chat import views as chat
from .seclea.views import *
from .donation.views import *
from .inverair.views import *
from .pardoewray.views import *


# ---------------------- FORMATING FUNCTIONS / THESE ARE NOT VIEWS --------------------- #
def main(file_path):
    return 'global/build/{file_path}'.format(file_path=file_path)


# ------------------------------ GLOBAL CLIENT CORE VIEWS ------------------------------ #
def index(req, *args, **kwargs):
    return render(req, main('index'))


def robots(req, *args, **kwargs):
    return render(req, main('robots.txt'), content_type='text/plain')


def manifestJSON(req, *args, **kwargs):
    return render(req, main('manifest.json'), content_type='application/json')


def asset_manifest(req, *args, **kwargs):
    return render(req, main('asset-manifest.json'), content_type='application/json')


def service_worker(req, *args, **kwargs):
    return render(
        req,
        main('service-worker.js'),
        content_type="application/x-javascript"
    )


def service_worker_map(req, *args, **kwargs):
    return render(
        req,
        main('service-worker.js.map'),
        content_type="application/x-javascript"
    )
