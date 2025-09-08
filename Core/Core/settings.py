import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "unsafe-secret-key") 
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS =  [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',


	# third-party
    'django.contrib.sites',
    'allauth',
    'allauth.socialaccount',
    'allauth.socialaccount.providers',
    'allauth.socialaccount.providers.instagram',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.twitter',
	# custom TikTok provider
    'phonenumber_field',

    # local
    'accounts',
    #other apps
    'posts'
]


MIDDLEWARE = [ 'django.middleware.security.SecurityMiddleware', 'django.contrib.sessions.middleware.SessionMiddleware', 'django.middleware.common.CommonMiddleware', 'django.middleware.csrf.CsrfViewMiddleware', 'django.contrib.auth.middleware.AuthenticationMiddleware', 'django.contrib.messages.middleware.MessageMiddleware', 'django.middleware.clickjacking.XFrameOptionsMiddleware', ]

ROOT_URLCONF = 'Core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# required by allauth
# 'django.contrib.auth.context_processors.auth',
# 'django.template.context_processors.csrf',
# 'django.contrib.messages.context_processors.messages'

WSGI_APPLICATION = 'Core.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Custom user model
AUTH_USER_MODEL = 'accounts.User'

# Password validation

AUTH_PASSWORD_VALIDATORS = [ { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator' }, { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator' }, { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator' }, { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator' }, ]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True 
USE_TZ = True
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = 'static/' 
STATICFILES_DIRS = [BASE_DIR / 'static'] 
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Allauth configuration

SITE_ID = 1 
LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL = "dashboard"
LOGOUT_REDIRECT_URL = "account_login"
ACCOUNT_USERNAME_REQUIRED = True 
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'optional'
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'  # extended with phone by backend ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True ACCOUNT_FORMS = { 'login': 'allauth.account.forms.LoginForm' }

# Authentication backends

AUTHENTICATION_BACKENDS = [
    'accounts.backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
]


# Social account providers config

SOCIALACCOUNT_PROVIDERS = { 'facebook': { 'METHOD': 'oauth2', 'SCOPE': ['email'], 'FIELDS': [ 'id', 'email', 'name', 'first_name', 'last_name', 'picture.type(large)' ], 'VERIFIED_EMAIL': False, 'VERSION': 'v12.0', }, 'twitter': { 'SCOPE': ['email', 'profile'], 'AUTH_PARAMS': {'force_login': 'true'}, }, 'instagram': { 'SCOPE': ['user_profile', 'user_media'], 'AUTH_PARAMS': {'response_type': 'code'}, }, 'tiktok': { 'SCOPE': ['user.info.basic'], 'AUTH_PARAMS': {'response_type': 'code'}, 'APP': { 'client_id': os.environ.get('TIKTOK_CLIENT_ID', ''), 'secret': os.environ.get('TIKTOK_CLIENT_SECRET', ''), 'key': ''}}}