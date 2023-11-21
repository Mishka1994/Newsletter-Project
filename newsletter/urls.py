from django.urls import path
from django.views.decorators.cache import cache_page

from newsletter.apps import NewsletterConfig
from newsletter.views import BaseTemplateView, NewsletterCreateView, NewsletterDetailView, NewsletterListView, \
    NewsletterUpdateView, NewsletterDeleteView, start_newsletter, ClientListView, MailingLogsListView, \
    LaunchNewsletterList, deactivate_newsletter

app_name = NewsletterConfig.name


urlpatterns = [
    path('', cache_page(60)(BaseTemplateView.as_view()), name='index'),
    path('create_newsletter/', NewsletterCreateView.as_view(), name='create_newsletter'),
    path('view_newsletter/<int:pk>/', NewsletterDetailView.as_view(), name='view_newsletter'),
    path('list_newsletter', NewsletterListView.as_view(), name='list_newsletter'),
    path('edit_newsletter/<int:pk>/', NewsletterUpdateView.as_view(), name='edit_newsletter'),
    path('delete_newsletter/<int:pk>/', NewsletterDeleteView.as_view(), name='delete_newsletter'),
    path('start_newsletter/<int:pk>/', start_newsletter, name='start_newsletter'),
    path('list_client/', ClientListView.as_view(), name='list_client'),
    path('list_mailinglogs/', MailingLogsListView.as_view(), name='list_mailinglogs'),
    path('list_launch_newsletters/', LaunchNewsletterList.as_view(), name='list_launch_newsletter'),
    path('deactivate_newsletter/<int:pk>/', deactivate_newsletter, name='deactivate_newsletter'),



]
