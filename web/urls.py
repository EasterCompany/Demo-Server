# Essential
from django.urls import path

# Application Views
from core.views import *
from tools.server.api import *

# URL Endpoints
urlpatterns = [

    # Global App
    path('', index),
    path('index.html', index),
    path('robots.txt', robots),
    path('manifest.json', manifestJSON),
    path('asset-manifest.json', asset_manifest),

    # Global App Service Worker
    path('service-worker.js', service_worker),
    path('service-worker.js.map', service_worker_map),

    # Chat App
    path('echat.app', chat.app),
    path('echat/manifest.json', chat.manifestJSON),
    path('echat/asset-manifest.json', chat.asset_manifest),

    # Seclea App
    path('seclea.app', seclea_app),
    path('seclea/manifest.json', seclea_manifestJSON),
    path('seclea/asset-manifest.json', seclea_asset_manifest),

    # Inverair App
    path('inverair.app', inverair_app),
    path('inverair/manifest.json', inverair_manifestJSON),
    path('inverair/asset-manifest.json', inverair_asset_manifest),

    # DoNation App
    path('donation.app', donation_app),
    path('donation/manifest.json', donation_manifestJSON),
    path('donation/asset-manifest.json', donation_asset_manifest),

    # OLT Server Admin API
    path('api/olt/status', OLT_status_api),
    path('api/olt/upgrade', OLT_upgrade_request_api),

]
