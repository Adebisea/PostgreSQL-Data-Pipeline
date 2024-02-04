import pandas as pd
from sqlalchemy_pipeline import create_sql_engine

def retrieve_UKdata():

 
    engine = create_sql_engine()
    query = ''' 
                select * from onlineretail where country = 'United Kingdom' LIMIT 100
            '''    
    df = pd.read_sql(sql=query,con=engine)

    #save data from United kingdom to file
    df.to_csv('ukretail.csv', index=False)


if __name__ == '__main__':

    retrieve_UKdata()
