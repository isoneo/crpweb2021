import os, sys
if os.environ['COMPUTERNAME'] == "AMDWILLHQ":
    prj_dir = "D:\Scripts\webdev\crpweb2021/backend"
    base_file_loc = "D:/Scripts/webdev/crpweb2021/setup_related/user_create"
    psql_host="192.168.0.180"
    psql_conn_db="crpweb_v2"
else:
    prj_dir="C:\scripts\www\capybara"
    base_file_loc = "C:/scripts/www/capybara/capybara/initial_data/user_create"
    psql_host="SQL"
    psql_conn_db = "crpweb_v2"


psql_user="spotfireuser"
psql_password="password"


sys.path.append(prj_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'core.dj_settings.settings_dev'
import django
django.setup()

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.conf import settings
from sqlalchemy import create_engine
#sys.path.append('X:/www/crpweb')
# from user_accounts_app.model_custom_user import Gondor_mgmt
import csv
import pandas as pd


user_list=[]
# with open('','rb') as f:
#     reader=csv.reader(f)
#     for row in reader:


rawcsvfile="email_export.csv"
tdf = pd.read_csv(base_file_loc + "/" + rawcsvfile)
rtdf=tdf.values.tolist()


# for i in rtdf:
#     user_sl=User(username=i['username'],
#                  email=i['email'],
#                  first_name=i['first_name'],
#                  last_name=i[last_name],
#                  password=make_password(i['password']),
#                  is_active=True,)
#     user_list.append(user_sl)


# for index, row in tdf.iterrows():
#     user_sl=User(username=row['username'],
#                  email=row['email'],
#                  first_name=row['first_name'],
#                  last_name=row['last_name'],
#                  password=make_password(row['password']),
#                  is_active=True,)
#     user_list.append(user_sl)
#
# User.objects.bulk_create(user_list)

for index, row in tdf.iterrows():
    user_sl = User.objects.create_user(row['username'], row['email'], row['password'])
    user_sl.last_name = row['last_name']
    user_sl.first_name = row['first_name']
    user_sl.is_active = True
    user_sl.save()
    # gondor_rcd = Gondor_mgmt(rcd_user=user_sl)
    # gondor_rcd.save()

sup_user = User.objects.create_user("admin", "william@crpok.com", "password")
sup_user.last_name = "NoLastName"
sup_user.first_name = "Admin"
sup_user.is_active = True
sup_user.is_staff = True
sup_user.is_superuser = True
sup_user.save()


# import psycopg2
# from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT # <-- ADD THIS LINE
engine = create_engine('postgresql+psycopg2://' + psql_user + ":" + psql_password + '@' + psql_host + '/' + psql_conn_db)
def eng_execute(engine,sql_query):
    connection = engine.raw_connection()
    cursor = connection.cursor()
    cursor.execute(sql_query)
    cursor.execute("commit;")
    cursor.close()


eng_execute(engine,
            """INSERT INTO gondor_mgmt(rcd_user_id)
            SELECT id FROM auth_user  
            """)
