# Local app imports
from api.pardoewray import email
from web.settings import SECRET_KEY
# Django imports imports
from urllib.parse import unquote
from django.http import JsonResponse
# Database model imports
from api.pardoewray.models import Jobs, JobRequirements


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


def parse_data(obj, reqs=[]):
    requirements = []
    for r in reqs:
        requirements.append(r.required)
    return {
        'title': obj.Title,
        'company': obj.Company,
        'website': obj.Website,
        'description': obj.Description,
        'location': obj.Location,
        'type': obj.Type,
        'date': str(obj.Date_Added).replace('-', '/'),
        'reqs': requirements
    }


def fetch_job_postings(req, *args, **kwargs):
    data = []
    for obj in Jobs.objects.all():
        data.append(parse_post(obj))
    return JsonResponse({'data': data})


def fetch_job_detail(req, uid, *args, **kwargs):
    data = Jobs.objects.filter(uid=uid).first()
    reqs = JobRequirements.objects.filter(uid=uid).all()
    return JsonResponse({
        uid: parse_data(data, reqs)
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
        if Jobs.objects.count() > 0:
            post_uid = int(Jobs.objects.first().id) + 1
        else:
            post_uid = 0
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


def update_post_reqs(req, uid, reqs, *args, **kwargs):
    if req.headers['Authorization'] == SECRET_KEY:
        rs = unquote(reqs).split(',')
        for r in rs:
            JobRequirements.objects.create(
                uid=unquote(uid),
                required=r.strip()
            )
        return JsonResponse({'status': 'OK'})
    return JsonResponse({'status': 'BAD'})


def user_apply(req, uid, fname, lname, umail, number, *args, **kwargs):
    return JsonResponse(email.service.send_application(
        job_id=unquote(uid),
        fname=unquote(fname),
        lname=unquote(lname),
        user_email=unquote(umail),
        user_mobile=unquote(number)
    ))
