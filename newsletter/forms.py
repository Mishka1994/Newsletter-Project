from django import forms

from newsletter.models import Newsletter


class DesignFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class NewsletterForm(DesignFormMixin, forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'
