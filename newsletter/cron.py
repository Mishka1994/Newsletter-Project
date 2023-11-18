from datetime import datetime
from django.conf import settings
from django.core.mail import send_mail
from newsletter.models import Newsletter, Client

CURRENT_TIME = datetime.now().time()
CURRENT_DATETIME = datetime.now()


def once_a_day_mailing():
    newsletter_list = Newsletter.objects.exclude(status_of_mailing='COMPLETE')
    for newsletter in newsletter_list:
        if newsletter.time_mailing <= CURRENT_TIME and newsletter.period == 'ONCE_DAY':
            for client in newsletter.client.all():
                send_mail(
                    subject=newsletter.message.message_subject,
                    message=newsletter.message.body_message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[f'{client}']
                )


def once_a_week_mailing():
    newsletter_list = Newsletter.objects.exclude(status_of_mailing='COMPLETE')
    for newsletter in newsletter_list:
        if newsletter.time_mailing <= CURRENT_TIME and newsletter.period == 'ONCE_WEEK':
            for client in newsletter.client.all():
                send_mail(
                    subject=newsletter.message.message_subject,
                    message=newsletter.message.body_message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[f'{client}']
                )


def once_a_month_mailing():
    newsletter_list = Newsletter.objects.exclude(status_of_mailing='COMPLETE')
    for newsletter in newsletter_list:
        if newsletter.time_mailing <= CURRENT_TIME and newsletter.period == 'ONCE_MONTH':
            for client in newsletter.client.all():
                send_mail(
                    subject=newsletter.message.message_subject,
                    message=newsletter.message.body_message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[f'{client}']
                )


def check_complete_mailing():
    newsletter_list = Newsletter.objects.exclude(status_of_mailing='COMPLETE')
    for newsletter in newsletter_list:
        if newsletter.end_of_mailing <= CURRENT_DATETIME:
            newsletter.status_of_mailing = 'COMPLETE'

