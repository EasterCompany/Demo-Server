# Essential
from django.urls import path, re_path

# Application Views
from .views import *
from core.views import *

urlpatterns = [
    # Pardoewray App
    path('manifest.json', pardoewray_manifestJSON),
    path('asset-manifest.json', pardoewray_asset_manifest),
    re_path(r'.*$', pardoewray_app, name='pardoewray'),

    # Pardoewray API
    path('api/news', fetch_news),
    path('api/jobs', fetch_job_postings),
    path('api/news/<str:pid>', fetch_post),
    path('api/jobs/<str:uid>', fetch_job_detail),
    path(
        'api/jobs/apply/<str:uid>/<str:fname>/<str:lname>/<str:umail>/<str:number>',
        user_apply
    ),
    path('api/admin/news/create/<str:title>/<str:content>', create_news),
    path('api/admin/jobs', fetch_job_postings_admin),
    path('api/admin/jobs/delete/<str:uid>', delete_job_post_admin),
    path(
        'api/admin/jobs/create/<str:title>/<str:company>/<str:website>/<str:location>/<str:jType>',
        create_new_post
    ),
    path(
        'api/admin/jobs/update/desc/<str:uid>/<str:description>',
        update_post_desc
    ),
    path(
        'api/admin/jobs/update/reqs/<str:uid>/<str:reqs>',
        update_post_reqs
    ),
]
