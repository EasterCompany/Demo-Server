# Django module imports
from django.urls import path, re_path
from django.shortcuts import render


# ---------------------- FORMATING FUNCTIONS / THESE ARE NOT VIEWS --------------------- #
def main(file_path):
    return 'global/build/{file_path}'.format(file_path=file_path)


# ------------------------------ GLOBAL CLIENT CORE VIEWS ------------------------------ #
def react(req, *args, **kwargs):
    return render(req, main('index'))


def robots(req, *args, **kwargs):
    return render(req, main('robots.txt'), content_type='text/plain')


def manifest(req, *args, **kwargs):
    return render(req, main('manifest.json'), content_type='application/json')


def assets(req, *args, **kwargs):
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


APP = [
    path('manifest.json', manifest),
    path('asset-manifest.json', assets),
    re_path(r'.*$', react, name='App Browser'),
]
