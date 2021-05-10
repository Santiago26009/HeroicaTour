from pathlib import Path
import os
import dj_database_url
from decouple import config

DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dhdaiftirqa8u',
        'USER': 'qqagrekfrnlpsj',
        'PASSWORD':'33b650a81cd548984bf8c505b32e46006cc3c9dcf201a2346d69225edf64b835',
        'HOST': 'ec2-3-91-127-228.compute-1.amazonaws.com',
        'PORT': 5432
    }
}