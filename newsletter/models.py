from django.db import models


class Message(models.Model):
    message_subject = models.CharField(max_length=100, verbose_name='Тема письма')
    body_message = models.TextField(verbose_name='Тело письма')

    def __str__(self):
        return f'{self.message_subject}'

    class Meta:
        verbose_name = 'Письмо'
        verbose_name_plural = 'Письма'

