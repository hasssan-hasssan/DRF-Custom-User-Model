import os
from pathlib import Path
from dotenv import load_dotenv
from datetime import timedelta

# Load environment variables
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG") == "True"


ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # Django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

INSTALLED_APPS += [
    # Third-Party apps
    "rest_framework",
    "rest_framework_simplejwt",
    "jwt_passwordless",
]

INSTALLED_APPS += [
    # My apps
    "accounts.apps.AccountsConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "backend.wsgi.application"


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_URL = "static/"


# Configure Django restframework
# REST_FRAMEWORK = {
#     "DEFAULT_AUTHENTICATION_CLASSES": (
#         "rest_framework_simplejwt.authentication.JWTAuthentication"
#     )
# }


# Configure Jwt passwordless
PASSWORDLESS_AUTH = {
    # Authentication types - 'EMAIL', 'MOBILE', or both
    "PASSWORDLESS_AUTH_TYPES": ["EMAIL"],
    # Token expiry time in seconds (default: 15 minutes)
    "PASSWORDLESS_TOKEN_EXPIRE_TIME": 15 * 60,
    # Email settings
    "PASSWORDLESS_EMAIL_NOREPLY_ADDRESS": "noreply@example.com",
    "PASSWORDLESS_EMAIL_SUBJECT": "Your Login Token",
    "PASSWORDLESS_EMAIL_PLAINTEXT_MESSAGE": "Enter this token to sign in: %s",
    # Optional: customize token length (3-6 digits)
    "PASSWORDLESS_TOKEN_LENGTH": 6,
    # Optional: Mark email as verified after successful authentication
    "PASSWORDLESS_USER_MARK_EMAIL_VERIFIED": True,
    "PASSWORDLESS_USER_EMAIL_VERIFIED_FIELD_NAME": "is_verified",
    # Optional: For SMS authentication
    # 'PASSWORDLESS_AUTH_TYPES': ['EMAIL', 'MOBILE'],
    # 'PASSWORDLESS_MOBILE_NOREPLY_NUMBER': '+15551234567',
    # 'PASSWORDLESS_MOBILE_MESSAGE': "Your login code is: %s",
}


# Configure djangorestframework-simplejwt
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}


# My settings
AUTH_USER_MODEL = "accounts.CustomUser"


# Configure Email backend
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
DEFAULT_FROM_EMAIL = "noreply@example.com"
