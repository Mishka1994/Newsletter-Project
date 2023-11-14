from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView, ListView, UpdateView, DeleteView
from newsletter.models import Newsletter
from newsletter.forms import NewsletterForm


class BaseTemplateView(TemplateView):
    template_name = 'newsletter/index.html'


class NewsletterCreateView(CreateView):
    model = Newsletter
    form_class = NewsletterForm
    success_url = reverse_lazy('newsletter:index')


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
