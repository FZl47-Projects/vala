from config.settings.base import BASE_DIR
from os import getenv


# Sqlite3 database config
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / getenv('SQLITE_PATH', 'db.sqlite3'),
    }
}
