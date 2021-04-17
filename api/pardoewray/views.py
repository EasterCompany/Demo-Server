# Django imports imports
from django.core import serializers
from django.http import JsonResponse
# Database model imports
from api.pardoewray.models import Jobs


def parse_post(obj):
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
