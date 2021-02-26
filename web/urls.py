# Essential
from django.urls import path

# Application Views
from core.views import *

# URL Endpoints
urlpatterns = [

    # Global App
    path('', index),
    path('index.html', index),
    path('robots.txt', robots),
    path('manifest.json', manifestJSON),
    path('asset-manifest.json', asset_manifest),

    # Seclea App
    path('seclea/', seclea_app),
    path('seclea/manifest.json', seclea_manifestJSON),
    path('seclea/asset-manifest.json', seclea_asset_manifest),

]
