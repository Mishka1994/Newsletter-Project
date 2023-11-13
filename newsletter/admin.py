from django.contrib import admin

from newsletter.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('message_subject', 'body_message',)
    list_filter = ('message_subject',)
    search_fields = ('message_subject', 'body_message',)
