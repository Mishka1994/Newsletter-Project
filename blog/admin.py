from django.contrib import admin

from blog.models import Blog


# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'article_content', 'number_of_views', 'publication_date',)
    list_filter = ('number_of_views', 'publication_date',)
    search_fields = ('title', 'article_content')
