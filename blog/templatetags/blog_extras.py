from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(is_safe=True)
@stringfilter
def parseme(value, arg):
    if len(value)<int(arg):
        return '%s'%value
    else:
        return '%s'%(value[:int(arg)] + '... (Read More)')
