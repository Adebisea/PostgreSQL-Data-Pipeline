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





if __name__ == "__main__":

    host= os.getenv('host')
    port= os.getenv('port')
    dbname= os.getenv('dbname')
    user= os.getenv('user')
    password= os.getenv('password')


