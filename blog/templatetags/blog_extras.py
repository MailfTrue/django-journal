from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(is_safe=True)
@stringfilter
def parseme(value, max_length):
    if len(value) > int(max_length):
        new_val = value[:int(max_length)]
        if not len(value) == int(max_length) + 1 and value[int(max_length)+1]!=" ":
            new_val = new_val[:new_val.rfind(" ")]
            return '%s'%(new_val + ' ... (Read More)')
    return '%s'%value
