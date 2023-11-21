from smtplib import SMTPConnectError, SMTPRecipientsRefused, SMTPServerDisconnected
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin, PermissionRequiredMixin, LoginRequiredMixin
from django.core.cache import cache
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView, DetailView, ListView, UpdateView, DeleteView

from blog.models import Blog
from newsletter.cron import CURRENT_TIME, CURRENT_DATETIME
from newsletter.models import Newsletter, MailingLogs, Client
from newsletter.forms import NewsletterForm, ClientForm, MailingLogsForm


class BaseTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'newsletter/index.html'

    def get_context_data(self, *args):
        context = super().get_context_data()
        context['articles'] = Blog.objects.all()[:4]
        return context


class NewsletterCreateView(LoginRequiredMixin, CreateView):
    model = Newsletter
    form_class = NewsletterForm
    success_url = reverse_lazy('newsletter:index')

    def form_valid(self, form):
        if form.is_valid():
            newsletter = form.save()
            if newsletter.time_mailing < CURRENT_TIME and newsletter.end_of_mailing > CURRENT_DATETIME:
                newsletter.status_of_mailing = 'LAUNCHED'
                newsletter.save()
                for client in newsletter.client.all():
                    try:
                        send_mail(
                            subject=newsletter.message.message_subject,
                            message=newsletter.message.body_message,
                            from_email=settings.EMAIL_HOST_USER,
                            recipient_list=[f'{client}']
                        )
                    except SMTPConnectError:
                        server_response = 'Произошла ошибка при установлении соединения с сервером'
                        status_attempt = 'Неудачно'
                    except SMTPRecipientsRefused:
                        server_response = ' Все адреса получателей отказались.'
                        status_attempt = 'Неудачно'
                    except SMTPServerDisconnected:
                        server_response = 'Сервер неожиданно отключился.'
                        status_attempt = 'Неудачно'
                    else:
                        server_response = 'Все хорошо'
                        status_attempt = 'Успешно'
                    finally:
                        MailingLogs.objects.create(
                            datetime_last_mailing=str(CURRENT_DATETIME),
                            result_mailing=status_attempt,
                            answer_mailing_service=server_response,
                            newsletter=newsletter
                        )
            else:
                newsletter.status_of_mailing = 'CREATED'
                newsletter.save()

        return super().form_valid(form)


class NewsletterDetailView(LoginRequiredMixin, DetailView):
    model = Newsletter
    form_class = NewsletterForm
    success_url = reverse_lazy('newsletter:index')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        if settings.CACHE_ENABLED:
            key = f'subject_list_{self.object.pk}'
            subject_list = cache.get(key)
            if subject_list is None:
                subject_list =self.oblect.subject_set.all()
                cache.set(key, subject_list)
        else:
            subject_list = self.object.subject_set.all()

        context_data['subjects'] = subject_list
        return context_data




class NewsletterListView(LoginRequiredMixin, ListView):
    model = Newsletter
    form_class = NewsletterForm

    def get_queryset(self, queryset=None):
        queryset = super().get_queryset()
        if not self.request.user.is_staff:
            queryset = queryset.filter(creator=self.request.user)
        return queryset


class LaunchNewsletterList(ListView):
    model = Newsletter
    form_class = NewsletterForm

    def get_queryset(self):
        queryset = super().get_queryset().filter(
            status_of_mailing='LAUNCHED'
        )
        return queryset


class NewsletterUpdateView(LoginRequiredMixin, UpdateView):
    model = Newsletter
    form_class = NewsletterForm
    success_url = reverse_lazy('newsletter:list_newsletter')


class NewsletterDeleteView(LoginRequiredMixin, DeleteView):
    model = Newsletter
    success_url = reverse_lazy('newsletter:list_newsletter')


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    form_class = ClientForm


class MailingLogsListView(LoginRequiredMixin, ListView):
    model = MailingLogs
    form_class = MailingLogsForm


@login_required
def start_newsletter(request, pk):
    newsletter = Newsletter.objects.get(pk=pk)
    newsletter.status_of_mailing = 'LAUNCHED'
    newsletter.save()
    return redirect(reverse('newsletter:list_newsletter'))


def deactivate_newsletter(request, pk):
    newsletter = Newsletter.objects.get(pk=pk)
    newsletter.status_of_mailing = 'COMPLETE'
    newsletter.save()
    return redirect(reverse('newsletter:list_newsletter'))
