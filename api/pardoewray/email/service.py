# Standard library imports
import smtplib
# Local app imports
from web.settings import SECRET_DATA
# Database model imports
from api.pardoewray.models import Jobs


def send_application(job_id, fname, lname, user_email, user_mobile):
    job_app = Jobs.objects.get(uid=job_id)

    gmail_user = SECRET_DATA['EMAIL_USER']
    gmail_password = SECRET_DATA['EMAIL_PASS']

    sent_from = gmail_user
    to = [SECRET_DATA['EMAIL_USER'], ]
    subject = 'User Application ({job_id})'.format(job_id=job_id)

    body = """\
{job_title} - {job_company}

Name: {fname} {lname}
Email: {user_email}
Mobile: {user_mobile}

View Job Post:
https://www.pardoewray.com/jobs/{job_id}
""".format(
    job_title=job_app.Title,
    job_company=job_app.Company,
    job_id=job_id,
    fname=fname,
    lname=lname,
    user_email=user_email,
    user_mobile=user_mobile
)

    email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()
        return {'status': 'OK'}
    except Exception as e:
        return {
            'status': 'BAD',
            'error': str(e)
        }
