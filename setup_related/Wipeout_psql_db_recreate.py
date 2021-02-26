import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT # <-- ADD THIS LINE
import os, sys


curr_computer = os.environ['COMPUTERNAME']
if  curr_computer== "AMDWILLHQ":
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
# cur2.execute("create extension postgis;")
# cur2.execute("create extension postgis_raster;")
# cur2.execute("create extension postgis_topology;")
# cur2.execute("create extension postgis_sfcgal;")
# cur2.execute("create extension fuzzystrmatch;")
cur2.execute("create extension postgres_fdw;")
if curr_computer == "AMDWILLHQ":
      cur2.execute("""CREATE SERVER link_rs_energy
      FOREIGN DATA WRAPPER postgres_fdw
      OPTIONS (host '192.168.0.180', dbname 'rs_energy');""")
      cur2.execute("""CREATE USER MAPPING FOR PUBLIC
      SERVER link_rs_energy
      OPTIONS (user 'spotfireuser', password 'password');""")
else:
      cur2.execute("""CREATE SERVER link_rs_energy
      FOREIGN DATA WRAPPER postgres_fdw
      OPTIONS (host 'SQL', dbname 'rs_energy');""")
      cur2.execute("""CREATE USER MAPPING FOR PUBLIC
      SERVER link_rs_energy
      OPTIONS (user 'spotfireuser', password 'password');""")
cur2.execute("CREATE SCHEMA FINANCE;")
# cur2.execute("CREATE SCHEMA ACCT_SSI_IX;")
# cur2.execute("CREATE SCHEMA ACCT_SSI_X;")
# cur2.execute("CREATE SCHEMA ACCT_SSI_XI;")
# cur2.execute("CREATE SCHEMA ACCT_SSI_XI_FUND;")
cur2.execute("CREATE SCHEMA rs_energy;")
cur2.execute("CREATE SCHEMA ACCT_SSI_XII;")
# cur2.execute("CREATE SCHEMA ACCT_SSI_CMB;")
# cur2.execute("CREATE SCHEMA ARIES_IX_X;")
cur2.execute("CREATE SCHEMA ARIES_XII;")
# cur2.execute("CREATE SCHEMA ARIES_CMB;")
cur2.execute("""IMPORT FOREIGN SCHEMA public
FROM SERVER link_rs_energy
INTO rs_energy;""")



cur2.close()




con3 = psycopg2.connect(dbname=psql_db_name,
      user=psql_user, host=psql_host,
      password=psql_password)
con3.autocommit = True
con3.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT) # <-- ADD THIS LINE

cur3 = con3.cursor()
print("    Creating Local Well Complaetion ")
cur3.execute("""
CREATE MATERIALIZED VIEW public.local_rs_well_completion as
SELECT API_UWI
,Unformatted_API_UWI
,WellID
,CompletionID
,CompletionNumber
,WellName
,Country
,StateProvince
,County
,RSOperator
,RawOperator
,InitialOperator
,RSTicker
,RSWellServiceProvider
,RSProdWellType
,StateWellType
,RSRegion
,RSBasin
,RSPlay
,RSSubPlay
,RSInterval
,RSWellType
,RSSpacingAssumption
,RSWellStatus
,Trajectory
,Formation
,FirstProdDateTimestamp
,FirstProdDate
,Vintage
,Latitude
,Longitude
,Latitude_BH
,Longitude_BH
,TrueVerticalDepth_FT
,MeasuredDepth_FT
,LeaseNumber
,District
,Field
,Section
,Township
,Range
,Elevation_FT
,CurrentGasGatherer
,CurrentOilGatherer
,PermitApprovedDate
,SpudDate
,RigReleaseDate
,CompletionDate
,StateFileNumber
,RSFracJobType
,RSFluidType
,CompletionDesign
,CompletionTime_DAYS
,PermitToSpud_DAYS
,SpudToRigRelease_DAYS
,SpudToCompletion_DAYS
,SpudToSales_DAYS
,UpperPerf_FT
,LowerPerf_FT
,PerfInterval_FT
,LateralLength_FT
,FracStages
,RSProppantBrand
,ProppantLoading_LBSPerGAL
,RSProppantType
,ProppantIntensity_LBSPerFT
,Proppant_LBS
,TotalWaterPumped_GAL
,WaterIntensity_GALPerFT
,TotalFluidPumped_BBL
,RSCompInsertedDate
,TestDate
,PeakProd_BOE
,PeakGas_MCF
,PeakProd_MCFE
,PeakOil_BBL
,CumProd_BOE
,CumGas_MCF
,CumProd_MCFE
,CumOil_BBL
,TotalProducingMonths
,Block
,Platform
,WellPadID
,LastProducingMonth
,LastMonthLiquidsProduction_BBL
,LastMonthGasProduction_MCF
,LastMonthWaterProduction_BBL
,AverageStageSpacing_FT
,API_UWI_12
,Unformatted_API_UWI_12
,API_UWI_14
,Unformatted_API_UWI_14
,Meridian
,CoordinateSource
FROM rs_energy.WellCompletion
where country = 'us'
""")



cur3.close()
