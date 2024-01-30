from sqlalchemy import create_engine, text
from dotenv import load_dotenv       
import pandas as pd
load_dotenv()
import os

host =os.getenv('host')
username= os.getenv('user')
password = os.getenv('password')     
port = os.getenv('port')
db_name = os.getenv('dbname')        
 




def create_sql_engine():
    engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{db_name}', echo=True)
    return engine

def create_conn(query):
    engine = create_sql_engine()
    conn = engine.connect()
    conn.execute(text(query))
    conn.commit()
     
def create_table_greentrips():

    query = '''CREATE TABLE IF NOT EXISTS "greentrips" (
                    "vendorid" INTEGER,
                    "lpep_pickup_datetime" timestamp,
                    "lpep_dropoff_datetime" timestamp,
                    "store_and_fwd_flag" TEXT,
                    "ratecodeid" INTEGER,
                    "pulocationid" INTEGER,
                    "dolocationid" INTEGER,
                    "passenger_count" INTEGER,
                    "trip_distance" REAL,
                    "fare_amount" REAL,
                    "extra" REAL,
                    "mta_tax" REAL,
                    "tip_amount" REAL,
                    "tolls_amount" REAL,
                    "ehail_fee" REAL,
                    "improvement_surcharge" REAL,
                    "total_amount" REAL,
                    "payment_type" INTEGER,
                    "trip_type" INTEGER,
                    "congestion_surcharge" REAL)'''
    create_conn(query)


