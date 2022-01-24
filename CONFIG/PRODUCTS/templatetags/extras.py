from django import template
register = template.Library()

@register.filter()
def is_numeric (value):
    try:
        value+=1
        return True
    except:
        return False


