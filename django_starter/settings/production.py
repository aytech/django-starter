import os
from time import strftime

from .base import *

ALLOWED_HOSTS = [
    '0.0.0.0',
]

GRAPHIQL_AVAILABLE = False

DEBUG = False

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': 'LOG:%(levelname)s TIME: %(asctime)s MESSAGE: %(message)s PATHNAME: %(pathname)s'
        }
    },
    'handlers': {
        'file': {
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            'class': 'logging.FileHandler',
            'filename': APP_DIR / 'logs' / 'art_{}.log'.format(strftime('%Y_%m_%d')),
            'formatter': 'verbose',
        }
    },
    'loggers': {
        'django-starter': {
            'handlers': ['file'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            'propagate': False,
        },
    }
}
