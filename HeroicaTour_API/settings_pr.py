from pathlib import Path
import os
import dj_database_url
from decouple import config

DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd7h1j5v5oit3iu',
        'USER': 'xgqxdmongnceoh',
        'PASSWORD':'b8424c26f8edf906c89eca50892e45d637ae74f1baaa45b58a27da12f756245b',
        'HOST': 'ec2-54-224-194-214.compute-1.amazonaws.com',
        'PORT': 5432
    }
}