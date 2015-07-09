"""
WSGI config for bay_pirate_fishing project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from bay_pirate_fishing.settings import ENVIRONMENT

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bay_pirate_fishing.settings")

application = get_wsgi_application()

if ENVIRONMENT == 'PRODUCTION':
    from whitenoise.django import DjangoWhiteNoise
    application = DjangoWhiteNoise(application)
