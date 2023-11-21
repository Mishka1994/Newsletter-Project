from django.db import models

from newsletter.models import NULLABLE


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    article_content = models.TextField(verbose_name='Содержимое статьи')
    image = models.ImageField(upload_to='blog_preview/', verbose_name='Изображение', **NULLABLE)
    number_of_views = models.IntegerField(default=0, verbose_name='Количество просмотров')
    publication_date = models.DateField(auto_now_add=True, verbose_name='Дата публикации')

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'

    def __str__(self):
        return f'{self.title}'
