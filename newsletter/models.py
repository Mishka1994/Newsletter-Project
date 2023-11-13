from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Message(models.Model):
    message_subject = models.CharField(max_length=100, verbose_name='Тема письма')
    body_message = models.TextField(verbose_name='Тело письма')

    def __str__(self):
        return f'{self.message_subject}'

    class Meta:
        verbose_name = 'Письмо'
        verbose_name_plural = 'Письма'


class Client(models.Model):
    email = models.EmailField(verbose_name='e-mail клиента')
    full_name = models.CharField(max_length=100, verbose_name='ФИО клиента')
    comment = models.TextField(verbose_name='Комментарий', **NULLABLE)

    def __str__(self):
        return f'{self.comment}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
