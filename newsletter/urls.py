from django.urls import path

from newsletter.views import BaseTemplateView

urlpatterns = [
    path('', BaseTemplateView.as_view(), name='base_page'),
]
