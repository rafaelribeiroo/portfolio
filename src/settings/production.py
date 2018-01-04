from .local import *
import dj_database_url


DEBUG = config_decouple('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ['rafaelribeiroo.herokuapp.com', '.rafaelribeiroo.com']

ADMINS = [
    ('Rafael Ribeiro', 'pereiraribeirorafael@gmail.com')
]

MANAGERS = ADMINS

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

HOST_SCHEME = "https://"
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
