from django import template

register=template.Library()

@register.filter(name='chunks')
def chunks(lst, chunk_size):
    chunk=[]
    for i in lst:
        chunk.append(i)
        i+=1
        if i==chunk_size:
            yield chunk
            chunk=[]
    yield chunk