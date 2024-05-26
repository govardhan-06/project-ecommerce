from django import template

register=template.Library()

@register.simple_tag(name='getstatus')
def getstatus(status):
    update_status=['Cart Stage','Confirmed','Processed','Delivered','Rejected']
    return update_status[status]
