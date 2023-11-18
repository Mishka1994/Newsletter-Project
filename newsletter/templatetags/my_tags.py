from django import template

register = template.Library()


@register.simple_tag()
def once_day_newsletter():
    pass
