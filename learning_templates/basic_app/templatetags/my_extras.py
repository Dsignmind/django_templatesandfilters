from django import template
#custom django filters example
register = template.Library()


@register.filter
def cutter(value,arg):
    """
    This cuts out all values of arg from string template
    """
    return value.replace(arg,'')
