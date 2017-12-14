from .base import *  # noqa


MIDDLEWARE = MIDDLEWARE + ['whitenoise.middleware.WhiteNoiseMiddleware']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
