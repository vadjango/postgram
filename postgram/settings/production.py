from .base import *

DEBUG = False

ALLOWED_HOSTS = [os.getenv("WEBSITE_HOSTNAME")]
CSRF_TRUSTED_ORIGINS = [os.getenv("WEBSITE_HOSTNAME")]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3'
    }
}
