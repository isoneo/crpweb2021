import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT # <-- ADD THIS LINE
import os, sys
import pandas as pd
from sqlalchemy import create_engine
import shutil

if os.environ['COMPUTERNAME'] == "AMDWILLHQ":
    psql_host = '192.168.0.180'
    base_file_loc = "D:/www/capybara/capybara/initial_data/crpweb_db_backup"
    migration_base_folder= "D:/Scripts/webdev/crpweb2021/backend/core/migrations"
else:
    psql_host = "SQL2"
    base_file_loc = "C:/scripts/www/capybara/capybara/initial_data/crpweb_db_backup"
    migration_base_folder= "C:/scripts/www/capybara/capybara/core/migrations"


shutil.rmtree(migration_base_folder)
os.makedirs(migration_base_folder, exist_ok=True)

open(migration_base_folder+'/__init__.py','w').close()