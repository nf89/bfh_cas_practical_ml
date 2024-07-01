# Local imports
import pandas as pd
import pyodbc
from dotenv import dotenv_values
from sqlalchemy.engine import URL                                                                                                                                                                                                                                                                                                                                                                                                          
from sqlalchemy import create_engine                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
import sqlalchemy as sa 

def get_table(table_name):
    # Constants
    config = dict(dotenv_values(".env")) 

    connection_string = "DRIVER={ODBC Driver 17 for SQL Server};trusted_connection=yes;SERVER="+config["MSSQL_SERVER"]+";DATABASE="+config["MSSQL_DATABASE"]+";"                                                                                                                                                                                                                                                                               
    connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})    

    # connection_string = "mssql+pyodbc:///?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server&server=WSISRZ0089\SISP22t&database=Atelier_DM_DataDelivery_dev"                                                                                                                                                                                                                                                                                                                                                 
    engine = create_engine(connection_url) 

    # Define query
    query = f'SELECT * FROM {table_name} AS c'

    # Configure connection for linux
    with engine.begin() as conn:                                                                                                                                                                                                                                                                                                                                                                                                                   
        query = f"""                                                                                                                                                                                                                                                                                                                                                                                                                                   
            SELECT * FROM {table_name} AS c                                                                                                                                                                                                                                                                                                                                                                                        
        """                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
        df = pd.read_sql_query(sa.text(query), conn) 

    return df