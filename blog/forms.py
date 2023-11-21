from django import forms

from blog.models import Blog
from newsletter.forms import DesignFormMixin


class BlogForm(DesignFormMixin, forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
