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


