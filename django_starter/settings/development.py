import os
from time import strftime

from .base import *

ALLOWED_HOSTS = [
    '0.0.0.0',
    'localhost',
]

GRAPHIQL_AVAILABLE = True

DEBUG = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': 'LOG:%(levelname)s TIME: %(asctime)s MESSAGE: %(message)s PATHNAME: %(pathname)s'
        }
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue'
        }
    },
    'handlers': {
        'console': {
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'file': {
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
            'class': 'logging.FileHandler',
            'filename': APP_DIR / 'logs' / 'art_{}.log'.format(strftime('%Y_%m_%d')),
            'formatter': 'verbose',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
            'propagate': False,
        },
        'django-starter': {
            'handlers': ['file'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    }
}
