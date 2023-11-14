from django.db import models
from django.contrib import admin

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
        return f'{self.full_name}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Newsletter(models.Model):
    # Периодичность для рассылок
    ONCE_A_DAY = 'OD'
    ONCE_A_WEEK = 'OW'
    ONCE_A_MONTH = 'OM'

    frequency_of_mailing = [
        (ONCE_A_DAY, 'Раз в день'),
        (ONCE_A_WEEK, 'Раз в неделю'),
        (ONCE_A_MONTH, 'Раз в месяц')
    ]

    # Статусы для рассылок
    COMPLETED = 'COM'
    CREATED = 'CRE'
    LAUNCHED = 'LAU'
    statuses = [
        (COMPLETED, 'Завершена'),
        (CREATED, 'Создана'),
        (LAUNCHED, 'Запущена')
    ]

    time_mailing = models.DateTimeField(verbose_name='Время отправления')
    period = models.CharField(
        max_length=100,
        choices=frequency_of_mailing,
        verbose_name='Периодичность'
    )
    status_of_mailing = models.CharField(
        max_length=100,
        choices=statuses,
        verbose_name='Статус'
    )
    message = models.ForeignKey(Message, on_delete=models.PROTECT, verbose_name='Текст рассылки')
    client = models.ManyToManyField(Client, verbose_name='Клиент для рассылки', related_name='clients')

    def __str__(self):
        return f'{self.status_of_mailing}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
