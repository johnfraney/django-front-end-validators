from django import template
from django.template.loader import get_template
from front_end_validators.utils import get_transcrypt_version


register = template.Library()

transcrypt_version = get_transcrypt_version()
if transcrypt_version.startswith('3.6'):
    script_tag_template_path = 'front_end_validators/script_tag_transcrypt_36.html'
elif transcrypt_version.startswith('3.7'):
    script_tag_template_path = 'front_end_validators/script_tag_transcrypt_37.html'
script_tag_template = get_template(script_tag_template_path)


@register.inclusion_tag(script_tag_template)
def front_end_validators_js():
    return
