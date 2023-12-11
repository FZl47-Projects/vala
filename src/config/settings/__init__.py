from os import getenv
from .base import *


PRODUCTION = getenv('PRODUCTION', False)

if PRODUCTION:
    from .production import *
else:
    from .development import *
