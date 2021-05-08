# Essential
from django.urls import path

# Application Views
from .views import *

API = [

    # Pardoewray API
    path(r'news', fetch_news),
    path(r'jobs', fetch_job_postings),
    path(r'news/<str:pid>', fetch_post),
    path(r'jobs/<str:uid>', fetch_job_detail),
    path(
        r'jobs/apply/<str:uid>/<str:fname>/<str:lname>/<str:umail>/<str:number>',
        user_apply
    ),
    path(r'admin/news/create/<str:title>/<str:content>', create_news),
    path(r'admin/jobs', fetch_job_postings_admin),
    path(r'admin/jobs/delete/<str:uid>', delete_job_post_admin),
    path(
        r'admin/jobs/create/<str:title>/<str:company>/<str:website>/<str:location>/<str:jType>',
        create_new_post
    ),
    path(
        r'admin/jobs/update/desc/<str:uid>/<str:description>',
        update_post_desc
    ),
    path(
        r'admin/jobs/update/reqs/<str:uid>/<str:reqs>',
        update_post_reqs
    ),

]