"""
ASGI config for Brawl_Stars_Brawler_Picker project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Brawl_Stars_Brawler_Picker.settings')

application = get_asgi_application()
