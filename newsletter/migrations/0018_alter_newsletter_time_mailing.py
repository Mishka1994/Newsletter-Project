# Generated by Django 4.2.7 on 2023-11-18 20:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0017_alter_newsletter_time_mailing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='time_mailing',
            field=models.TimeField(default=datetime.datetime(2023, 11, 18, 20, 19, 8, 680894), verbose_name='Время рассылки'),
        ),
    ]
