from django import template

register=template.Library()

@register.simple_tag(name='subtotal')
def subtotal(a,b):
    return a*b