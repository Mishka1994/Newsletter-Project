from django.contrib.auth.models import AbstractUser
from django.db import models

from newsletter.models import NULLABLE


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Почта')
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE)

    code_for_verify = models.CharField(max_length=50, verbose_name='Код для верификации почты', **NULLABLE)
    is_active = models.BooleanField(default=False, verbose_name='Признак активности')

    class Meta:
        permissions = [
            (
                "set_is_active_status",
                "Can_active_user"
            )
        ]

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
