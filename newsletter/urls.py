from django.urls import path

from newsletter.apps import NewsletterConfig
from newsletter.views import BaseTemplateView, NewsletterCreateView, NewsletterDetailView, NewsletterListView, \
    NewsletterUpdateView, NewsletterDeleteView

app_name = NewsletterConfig.name


urlpatterns = [
    path('', BaseTemplateView.as_view(), name='index'),
    path('create_newsletter/', NewsletterCreateView.as_view(), name='create_newsletter'),
    path('view_newsletter/<int:pk>/', NewsletterDetailView.as_view(), name='view_newsletter'),
    path('list_newsletter', NewsletterListView.as_view(), name='list_newsletter'),
    path('edit_newsletter/<int:pk>/', NewsletterUpdateView.as_view(), name='edit_newsletter'),
    path('delete_newsletter/<int:pk>/', NewsletterDeleteView.as_view(), name='delete_newsletter'),

]
