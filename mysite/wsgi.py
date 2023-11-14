"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

### Keroku註解
# from django.core.wsgi import get_wsgi_application
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
# application = get_wsgi_application()

### Keroku新增
from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(application)