from .common import *

if ENVIRONMENT == 'PRODUCTION':
    try:
        from .production import *
    except ImportError:
        pass

elif ENVIRONMENT == 'DEVELOPMENT':
    try:
        from .dev import *
    except ImportError:
        pass
