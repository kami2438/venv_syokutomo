from django import template

register = template.Library()

@register.filter
def checked(value, querydict):
    kinds = querydict.get('category')
    print("hhhh",kinds)
    if str(value) in kinds:
        return "checked"
    return ""

@register.filter
def name(querydict):
    name = querydict.get('name')
    
    return "" if name is None else name