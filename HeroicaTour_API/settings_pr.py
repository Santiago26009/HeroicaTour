from pathlib import Path
import os
import dj_database_url
from decouple import config

DATABASES = {
    'default':{
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'd2red0rctb8vmo',
    'USER': 'cwxrrsrzadmqcj',
    'PASSWORD':'607b40da628cbc9fba622892e3a053fd82ba6a318572fc4e1dd7c2671367d36f',
    'HOST': 'ec2-23-23-128-222.compute-1.amazonaws.com',
    'PORT': 5432
    }
}