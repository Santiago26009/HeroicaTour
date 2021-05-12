from pathlib import Path
import os
import dj_database_url
from decouple import config

DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'depflul5qe545g',
        'USER': 'kutzhmshtuzbhi',
        'PASSWORD':'a799dd0023fb1c5495ee44fb845d998dec7e6dc6eb67f30ebf0b357fca3005db',
        'HOST': 'ec2-18-215-111-67.compute-1.amazonaws.com',
        'PORT': 5432
    }
}