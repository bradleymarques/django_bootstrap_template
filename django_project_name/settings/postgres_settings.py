import os
from .base_settings import *

print("HERE")
print("HERE")
print("HERE")
print("HERE")
print("HERE")
print("HERE")
print("HERE")
print("HERE")
print("HERE")
print("HERE")
print("HERE")
print("HERE")
print("HERE")
print("HERE")
print("HERE")
print("HERE")
print("HERE")
print("HERE")
print("HERE")
print("HERE")
print("HERE")
print("OK, VARIABLE TIME:")
print(os.environ.get('POSTGRES_DATABASE_NAME'))
print(os.environ.get('POSTGRES_USERNAME'))
print(os.environ.get('POSTGRES_PASSWORD'))
print(os.environ.get('POSTGRES_HOST'))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DATABASE_NAME'),
        'USER': os.environ.get('POSTGRES_USERNAME'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': os.environ.get('POSTGRES_HOST'),
        'PORT': 5432,
    }
}
