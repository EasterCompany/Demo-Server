# Local app imports
from web.settings import SECRET_KEY
# Django imports imports
from urllib.parse import unquote
from django.http import JsonResponse
from django.core.management.utils import get_random_secret_key
# Database model imports
from api.pardoewray.models import Jobs


def parse_post(obj):
    return {
        'uid': obj.uid,
        'title': obj.Title,
        'location': obj.Location,
        'type': obj.Type,
        'date': str(obj.Date_Added).replace('-', '/')
    }


def parse_post_admin(obj):
    return {
        'uid': obj.uid,
        'title': obj.Title,
        'company': obj.Company,
        'location': obj.Location,
        'type': obj.Type,
        'date': str(obj.Date_Added).replace('-', '/')
    }


def parse_data(obj):
    return {
        'title': obj.Title,
        'company': obj.Company,
        'website': obj.Website,
        'description': obj.Description,
        'location': obj.Location,
        'type': obj.Type,
        'date': str(obj.Date_Added).replace('-', '/')
    }


def fetch_job_postings(req, *args, **kwargs):
    data = []
    for obj in Jobs.objects.all():
        data.append(parse_post(obj))
    return JsonResponse({'data': data})


def fetch_job_detail(req, uid, *args, **kwargs):
    data = Jobs.objects.filter(uid=uid).first()
    return JsonResponse({
        uid: parse_data(data)
    })


def fetch_job_postings_admin(req, *args, **kwargs):
    data = []
    if req.headers['Authorization'] == SECRET_KEY:
        for obj in Jobs.objects.all():
            data.append(parse_post_admin(obj))
    return JsonResponse({'data': data})


def delete_job_post_admin(req, uid, *args, **kwargs):
    if req.headers['Authorization'] == SECRET_KEY:
        Jobs.objects.filter(uid=unquote(uid)).delete()
        return JsonResponse({'status': 'OK'})
    return JsonResponse({'status': 'BAD'})


def create_new_post(req, title, company, website, location, jType, *args, **kwargs):
    if req.headers['Authorization'] == SECRET_KEY:
        post_uid = int(Jobs.objects.first().id) + 1
        Jobs.objects.create(
            uid=post_uid,
            Title=unquote(title),
            Company=unquote(company),
            Website=unquote(website),
            Location=unquote(location),
            Type=unquote(jType),
        )
        return JsonResponse({
            'status': 'OK',
            'uid': post_uid
        })
    return JsonResponse({'status': 'BAD'})


def update_post_desc(req, uid, description, *args, **kwargs):
    if req.headers['Authorization'] == SECRET_KEY:
        j = Jobs.objects.get(uid=unquote(uid))
        j.Description = unquote(description)
        j.save()
        return JsonResponse({'status': 'OK'})
    return JsonResponse({'status': 'BAD'})
