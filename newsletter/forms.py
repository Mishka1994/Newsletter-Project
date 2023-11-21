from django import forms

from newsletter.models import Newsletter, Client, MailingLogs


class DesignFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class NewsletterForm(DesignFormMixin, forms.ModelForm):
    class Meta:
        model = Newsletter
        exclude = ('status_of_mailing', )


class ClientForm(DesignFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class MailingLogsForm(DesignFormMixin, forms.ModelForm):
    class Meta:
        model = MailingLogs
        fields = '__all__'
