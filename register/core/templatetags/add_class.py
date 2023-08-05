from django import template

register = template.Library()


@register.filter
def addclass(field, css):
    """Add css class"""
    return field.as_widget(attrs={'class': css})
