"""
ASGI config for Culture_and_history_of_Arkhangelsk project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Culture_and_history_of_Arkhangelsk.settings')

application = get_asgi_application()
