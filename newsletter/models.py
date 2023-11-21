from django.conf import settings
from django.db import models
from django.contrib import admin
from datetime import datetime

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
        return f'{self.email}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Newsletter(models.Model):
    # Периодичность для рассылок
    ONCE_A_DAY = 'ONCE_DAY'
    ONCE_A_WEEK = 'ONCE_WEEK'
    ONCE_A_MONTH = 'ONCE_MONT'

    frequency_of_mailing = [
        (ONCE_A_DAY, 'Раз в день'),
        (ONCE_A_WEEK, 'Раз в неделю'),
        (ONCE_A_MONTH, 'Раз в месяц')
    ]

    # Статусы для рассылок
    COMPLETED = 'COMPLETE'
    CREATED = 'CREATED'
    LAUNCHED = 'LAUNCHED'
    statuses = [
        (COMPLETED, 'Завершена'),
        (CREATED, 'Создана'),
        (LAUNCHED, 'Запущена')
    ]

    time_mailing = models.TimeField(default=datetime.now(), verbose_name='Время рассылки')
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
    end_of_mailing = models.DateTimeField(verbose_name='Дата и время окончание рассылки', default='2024-01-01 12:00')
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='Создатель рассылки',
                                **NULLABLE)

    def __str__(self):
        return f'{self.message}, {self.status_of_mailing}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class MailingLogs(models.Model):
    datetime_last_mailing = models.DateTimeField(auto_now=True, verbose_name='Дата и время последней рассылки')
    result_mailing = models.CharField(max_length=50, verbose_name='результат попытки')
    answer_mailing_service = models.CharField(max_length=255, verbose_name='Ответ почтового сервиса')
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE, verbose_name='Рассылка')

    class Meta:
        verbose_name = 'Набор логов'
        verbose_name_plural = 'Наборы логов'

    def __str__(self):
        return f'{self.result_mailing}'
