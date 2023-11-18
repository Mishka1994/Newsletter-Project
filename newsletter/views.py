from datetime import datetime

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView, DetailView, ListView, UpdateView, DeleteView

from newsletter.cron import CURRENT_TIME, CURRENT_DATETIME
from newsletter.models import Newsletter
from newsletter.forms import NewsletterForm


class BaseTemplateView(TemplateView):
    template_name = 'newsletter/index.html'


class NewsletterCreateView(CreateView):
    model = Newsletter
    form_class = NewsletterForm
    success_url = reverse_lazy('newsletter:index')

    def form_valid(self, form):
        if form.is_valid:
            newsletter = form.save()
            if newsletter.time_mailing >= CURRENT_TIME and newsletter.end_of_mailing > CURRENT_DATETIME:
                client_list = [client for client in newsletter.client.all()]
                send_mail(
                    subject=newsletter.message.message_subject,
                    message=newsletter.message.body_message,
                    from_email=settings.EMAL_HOST_USER,
                    recipient_list=client_list
                )
        return super().form_valid(form)


class NewsletterDetailView(DetailView):
    model = Newsletter
    form_class = NewsletterForm
    success_url = reverse_lazy('newsletter:index')


class NewsletterListView(ListView):
    model = Newsletter
    form_class = NewsletterForm


class NewsletterUpdateView(UpdateView):
    model = Newsletter
    form_class = NewsletterForm
    success_url = reverse_lazy('newsletter:index')


class NewsletterDeleteView(DeleteView):
    model = Newsletter
    success_url = reverse_lazy('newsletter:index')


def start_newsletter(request, pk):
    client_newsletter = Newsletter.objects.get(pk=pk)
    client_newsletter.status_of_mailing = 'LAUNCHED'
    client_newsletter.save()
    return redirect(reverse('newsletter:list_newsletter'))

