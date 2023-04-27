# Development settings
import os
from decouple import Csv, config
from .base import *


# SITE_ID = 1

DEBUG = True

SECRET_KEY = config("SECRET_KEY")

ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())
# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_NAME", ""),  # noqa
        "USER": os.environ.get("POSTGRES_USER", "postgres"),  # noqa
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", ""),  # noqa
        "HOST": os.environ.get("POSTGRES_HOST", ""),  # noqa
        "PORT": os.environ.get("POSTGRES_PORT", ""),
    }
}
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "static"

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"


# DEFAULT_FILE_STORAGE = config("DEFAULT_FILE_STORAGE", default="django.core.files.storage.FileSystemStorage")

# redis settings
REDIS_HOST = config("REDIS_HOST")
# REDIS_HOST = "redis"
REDIS_PORT = config("REDIS_PORT")
REDIS_DB = config("REDIS_DB")

# CELERY STUFF
CELERY_BROKER_URL = config("CELERY_BROKER_URL", default="redis://redis:6379")
CELERY_RESULT_BACKEND = config("CELERY_BROKER_URL", default="redis://redis:6379")
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = "UTC"

# Stripe Keys
STRIPE_PUBLISHABLE_KEY = config("STRIPE_PUBLISHABLE_KEY")
STRIPE_SECRET_KEY = config("STRIPE_SECRET_KEY")
STRIPE_API_VERSION = config("STRIPE_API_VERSION")
STRIPE_WEBHOOK_SECRET = config("STRIPE_WEBHOOK_SECRET")
