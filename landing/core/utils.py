from django.conf import settings
from django.template import loader, Context
from requests import post


def send_email(associate, title, template):
    t = loader.get_template(template)
    body = t.render({'associate': associate})

    url = 'https://api.mailgun.net/v3/mg.clubelife.com/messages'

    r = post(url, auth=('api', settings.MAILGUN_API_KEY), data={
        'from': 'do-not-reply@clube.life',
        'to': associate.user.email,
        'subject': title,
        'html': body
    })
