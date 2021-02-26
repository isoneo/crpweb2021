import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT # <-- ADD THIS LINE
import os, sys
import pandas as pd
from sqlalchemy import create_engine
import shutil

if os.environ['COMPUTERNAME'] == "AMDWILLHQ":
    psql_host = '192.168.0.180'
    base_file_loc = "D:/Scripts/webdev/crpweb2021/backend/"
    migration_base_folder= "D:/Scripts/webdev/crpweb2021/backend/"
else:
    psql_host = "SQL2"
    base_file_loc = "C:/scripts/www/capybara/capybara/initial_data/crpweb_db_backup"
    migration_base_folder= "C:/scripts/www/capybara/capybara/core/migrations"


def find_dir_with_name(base_dir, match_str):
    final_result = []
    for root, dir, filelist in os.walk(base_dir):
        # print(root)
        # print(dir)
        for sl_dir in dir:
            if sl_dir == match_str:  # insert logic to find the folder you want
                print(root+'/'+sl_dir)
                final_result.append(root+'/'+sl_dir)
    return final_result



migration_dir_ls = find_dir_with_name(base_file_loc,"migrations")

for mig_dir in migration_dir_ls:
    print("Cleaning  out "+mig_dir)
    shutil.rmtree(mig_dir)
    os.makedirs(mig_dir, exist_ok=True)

    open(mig_dir+'/__init__.py','w').close()