from django import template


register = template.Library()


@register.inclusion_tag('front_end_validators/script_tag.html')
def front_end_validators_js():
    return
