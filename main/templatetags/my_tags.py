from django import template
from django.templatetags.static import static

register = template.Library()

@register.filter()
def product_media(val):
    if val and hasattr(val, 'url'):
        return val.url
    return static('no_image.jpg')

