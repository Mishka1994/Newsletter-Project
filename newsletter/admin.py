from django.contrib import admin

from newsletter.models import Message, Client, Newsletter


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('message_subject', 'body_message',)
    list_filter = ('message_subject',)
    search_fields = ('message_subject', 'body_message',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'full_name', 'comment',)
    search_fields = ('email', 'full_name',)
    ordering = ('id',)


@admin.register(Newsletter)
class Newsletter(admin.ModelAdmin):
    list_display = ('id', 'time_mailing', 'period', 'status_of_mailing', 'message',)
    search_fields = ('status_of_mailing', 'client',)
    ordering = ('id',)
