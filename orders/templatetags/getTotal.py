from django import template

register=template.Library()

@register.simple_tag(name='getTotal')
def getTotal(cart):
    total=0
    for item in cart:
        total+=item.product.price*item.quantity
    return total