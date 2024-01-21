import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()

class Load_Data():

    def __init__(self,host,port,dbname,user,password):

        self.host = host
        self.port = port
        self.dbname = dbname
        self.user = user
        self.password = password

    def db_conn(self):
    #Connect to the postgres db

        try:
            connect = psycopg2.connect(
                host=self.host,
                port=self.port,
                dbname=self.dbname,
                user=self.user,
                password=self.password
                )
            return connect
        except psycopg2.Error as e:
            print('Error connecting to db:', e)

    def execute_queries(self, query):
        
        connect = self.db_conn()
        cursor = connect.cursor()
        try:
            cursor.execute(query)
            print('Query successfully executed')
        except psycopg2.Error as e:
            print('Error executing query:', e)

        connect.commit()
        cursor.close()
        connect.close()

    def create_table(self):

        query = '''CREATE TABLE IF NOT EXISTS onlineretail(
                        InvoiceNo varchar(10),
                        StockCode varchar(25),
                        Describe varchar(50),
                        Quantity int,
                        InvoiceDate timestamp,
                        UnitPrice real,
                        CustomerID int,
                        Country varchar(25))'''
        
        self.execute_queries(query)

        

if __name__ == "__main__":

    host= os.getenv('host')
    port= os.getenv('port')
    dbname= os.getenv('dbname')
    user= os.getenv('user')
    password= os.getenv('password')


