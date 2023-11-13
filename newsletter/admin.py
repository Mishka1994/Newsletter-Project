from django.contrib import admin

from newsletter.models import Message, Client


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('message_subject', 'body_message',)
    list_filter = ('message_subject',)
    search_fields = ('message_subject', 'body_message',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'comment',)
    list_filter = ('full_name',)
    search_fields = ('email', 'full_name',)
