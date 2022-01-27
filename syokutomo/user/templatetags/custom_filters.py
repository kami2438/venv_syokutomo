from django import template

register = template.Library()

@register.filter
def checked(value, querydict):
    kinds = querydict.getlist('kind')
    if str(value) in kinds:
        return "checked"
    return ""
