from django import template
from django.urls import reverse

from misago.conf import settings


register = template.Library()


@register.filter(name='avatar')
def avatar(user, size=200):
    found_avatar = user.avatars[0]
    for user_avatar in user.avatars:
        if user_avatar['size'] >= size:
            found_avatar = user_avatar
    return found_avatar['url']
