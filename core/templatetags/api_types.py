from django import template
from django.utils.safestring import SafeString

register = template.Library()

ELEMENT_COLOUR_MAPPINGS = {
    'get': 'text-green-500',
    'put': 'text-sky-500',
    'post': 'text-red-500',
    'delete': 'text-orange-500',
    'patch': 'text-yellow-500',
}

def api_type(type: str) -> SafeString:
    element_colour = ELEMENT_COLOUR_MAPPINGS[type.lower()]
    element = f''' 
    <p class="text-sm min-w-[51px] text-right {element_colour}" style=' font-weight: 900; font family: "Figtree"; '>{type.upper()}</p>
    '''
    return SafeString(element)

register.filter('api_type', api_type)

