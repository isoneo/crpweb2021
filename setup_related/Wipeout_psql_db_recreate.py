import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT # <-- ADD THIS LINE
import os, sys

if os.environ['COMPUTERNAME'] == "AMDWILLHQ":
      psql_host = '192.168.0.180'
else:
      psql_host = "SQL2"
psql_user="spotfireuser"
psql_password="password"

psql_conn_db = "postgres"
psql_db_name ="crpweb_v2"

con = psycopg2.connect(dbname=psql_conn_db,
      user=psql_user, host=psql_host,
      password=psql_password)
con.autocommit = True
con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT) # <-- ADD THIS LINE

cur = con.cursor()
cur.execute("select pg_terminate_backend(pid) from pg_stat_activity where datname= '%s' ;" % psql_db_name)
cur.execute("DROP DATABASE %s ;" % psql_db_name)
cur.execute("CREATE DATABASE %s  ;" % psql_db_name)
cur.close()


con2 = psycopg2.connect(dbname=psql_db_name,
      user=psql_user, host=psql_host,
      password=psql_password)
con2.autocommit = True
con2.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT) # <-- ADD THIS LINE

cur2 = con2.cursor()
cur2.execute("CREATE SCHEMA FINANCE;")
# cur2.execute("CREATE SCHEMA ACCT_SSI_IX;")
# cur2.execute("CREATE SCHEMA ACCT_SSI_X;")
# cur2.execute("CREATE SCHEMA ACCT_SSI_XI;")
# cur2.execute("CREATE SCHEMA ACCT_SSI_XI_FUND;")
cur2.execute("CREATE SCHEMA ACCT_SSI_XII;")
# cur2.execute("CREATE SCHEMA ACCT_SSI_CMB;")
# cur2.execute("CREATE SCHEMA ARIES_IX_X;")
cur2.execute("CREATE SCHEMA ARIES_XII;")
# cur2.execute("CREATE SCHEMA ARIES_CMB;")

cur2.close()