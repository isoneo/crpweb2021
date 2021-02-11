import os
from .base import *

DEBUG=True

AUTH_PASSWORD_VALIDATORS = [

]


SECURE_SSL_REDIRECT = False


if os.environ['COMPUTERNAME'] in ['AMDWILLHQ', 'WILLHQ']:
    engine_str = 'django.db.backends.postgresql_psycopg2'
    MEDIA_ROOT = "D:/www/test_mediafiles"


else:
    engine_str = 'django.db.backends.postgresql_psycopg2'
    MEDIA_ROOT = "//spotfire/e/www/test_mediafiles"
    # engine_str = 'django.contrib.gis.db.backends.postgis'
psql_db_name = 'crpweb_v2'

DATABASES = {
    'default': {
        # 'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'ENGINE': engine_str,
        'NAME': psql_db_name,
        'USER': POSTGRES_DB_user,
        'PASSWORD': POSTGRES_DB_pd,
        'HOST': POSTGRES_DB_HOST,
        'PORT': '',
    },
    'rs_data': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'rs_energy',
        'USER': POSTGRES_DB_user,
        'PASSWORD': POSTGRES_DB_pd,
        'HOST': POSTGRES_DB_HOST,
        'PORT': '',
    },
    # 'FINANCE': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': 'FINANCE',
    #     'USER': POSTGRES_DB_user,
    #     'PASSWORD': POSTGRES_DB_pd,
    #     'HOST': POSTGRES_DB_HOST,
    #     'PORT': '',
    # },
    # 'acc_ssi_ix': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'OPTIONS':{'options': '-c search_path=acct_ssi_ix'},
    #     'NAME': psql_db_name,
    #     'USER': POSTGRES_DB_user,
    #     'PASSWORD': POSTGRES_DB_pd,
    #     'HOST': POSTGRES_DB_HOST,
    #     'PORT': '',
    # },
    # 'acc_ssi_x': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'OPTIONS':{'options': '-c search_path=acct_ssi_x'},
    #     'NAME': psql_db_name,
    #     'USER': POSTGRES_DB_user,
    #     'PASSWORD': POSTGRES_DB_pd,
    #     'HOST': POSTGRES_DB_HOST,
    #     'PORT': '',
    # },
    # 'acc_ssi_xi': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'OPTIONS':{'options': '-c search_path=acct_ssi_xi'},
    #     'NAME': psql_db_name,
    #     'USER': POSTGRES_DB_user,
    #     'PASSWORD': POSTGRES_DB_pd,
    #     'HOST': POSTGRES_DB_HOST,
    #     'PORT': '',
    # },
    # 'acc_ssi_xii': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'OPTIONS':{'options': '-c search_path=acct_ssi_xii'},
    #     'NAME': psql_db_name,
    #     'USER': POSTGRES_DB_user,
    #     'PASSWORD': POSTGRES_DB_pd,
    #     'HOST': POSTGRES_DB_HOST,
    #     'PORT': '',
    # },
    # 'acc_ssi_xi_fund': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'OPTIONS': {'options': '-c search_path=acct_ssi_xi_fund'},
    #     'NAME': psql_db_name,
    #     'USER': POSTGRES_DB_user,
    #     'PASSWORD': POSTGRES_DB_pd,
    #     'HOST': POSTGRES_DB_HOST,
    #     'PORT': '',
    # },
    # 'acc_ssi_cmb': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'OPTIONS': {'options': '-c search_path=acct_ssi_cmb'},
    #     'NAME': psql_db_name,
    #     'USER': POSTGRES_DB_user,
    #     'PASSWORD': POSTGRES_DB_pd,
    #     'HOST': POSTGRES_DB_HOST,
    #     'PORT': '',
    # },
    # 'aries_ix_x': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'OPTIONS':{'options': '-c search_path=aries_ix_ix'},
    #     'NAME': psql_db_name,
    #     'USER': POSTGRES_DB_user,
    #     'PASSWORD': POSTGRES_DB_pd,
    #     'HOST': POSTGRES_DB_HOST,
    #     'PORT': '',
    # },
    # 'aries_xi': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'OPTIONS': {'options': '-c search_path=aries_xi'},
    #     'NAME': psql_db_name,
    #     'USER': POSTGRES_DB_user,
    #     'PASSWORD': POSTGRES_DB_pd,
    #     'HOST': POSTGRES_DB_HOST,
    #     'PORT': '',
    # },
    # 'HEDGEDB': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': 'hedge_db',
    #     'USER': POSTGRES_DB_user,
    #     'PASSWORD': POSTGRES_DB_pd,
    #     'HOST': POSTGRES_DB_HOST,
    #     'PORT': '',
    # },
    # 'SQL': {
    #     'ENGINE': 'sqlserver_ado',
    #     'NAME': 'DEVELOPMENT2',
    #     'USER': mssql_user,
    #     'PASSWORD': mssql_password,
    #     'HOST': mssql_host,
    #     'PORT': '1433',
    # },


}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

### File Upload / Media Settings
# MEDIA_ROOT="A:/webfileuploads/"
# MEDIA_ROOT="//spotfire/e/www/test_mediafiles/"
# # MEDIA_ROOT="X:/crpweb_files/"
# MEDIA_URL="/media/"
#
#
#
# ROOT_URLCONF = 'crpweb.urls'