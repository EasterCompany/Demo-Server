# Essential
from django.urls import path, re_path

# Application Views
from api.views import *
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
    path('messages', chat.app),
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

    # Pardoewray App
    path('pardoewray/manifest.json', pardoewray_manifestJSON),
    path('pardoewray/asset-manifest.json', pardoewray_asset_manifest),
    re_path(r'pardoewray/.*$', pardoewray_app, name='pardoewray'),

    # Pardoewray API
    path('api/jobs', pardoewrayAPI.fetch_job_postings),
    path('api/jobs/<str:uid>', pardoewrayAPI.fetch_job_detail),
    path(
        'api/jobs/apply/<str:uid>/<str:fname>/<str:lname>/<str:umail>/<str:number>',
        pardoewrayAPI.user_apply
    ),
    path('api/admin/jobs', pardoewrayAPI.fetch_job_postings_admin),
    path('api/admin/jobs/delete/<str:uid>', pardoewrayAPI.delete_job_post_admin),
    path(
        'api/admin/jobs/create/<str:title>/<str:company>/<str:website>/<str:location>/<str:jType>',
        pardoewrayAPI.create_new_post
    ),
    path(
        'api/admin/jobs/update/desc/<str:uid>/<str:description>',
        pardoewrayAPI.update_post_desc
    ),
    path(
        'api/admin/jobs/update/reqs/<str:uid>/<str:reqs>',
        pardoewrayAPI.update_post_reqs
    ),

    # OLT Server Admin API
    path('api/olt/status', OLT_status_api),
    path('api/olt/upgrade', OLT_upgrade_request_api),

    # Login API
    path('api/login', login.views.user),
    path('api/admin', login.views.admin),
    path('api/login/verify', login.views.verify),

    # Register API
    path('api/register', new_user.views.register_new_user),
    path('api/register/verify', new_user.views.check_email_exists)

]
