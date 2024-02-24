"""
database.py - Contains the database connection and communication functions.

Exports the connect() function to initialize a connection to the PostgreSQL database.
Also contains __main__ block to load config and connect if run directly.
"""
#!/usr/bin/env python 
"""Contains the database connection and all communication with the database"""
import psycopg2
from config import load_config

def connect(config):
    """ Connect to the PostgreSQL database server and create table qrcodes2 """
    try:
        # connecting to the PostgreSQL server
        with psycopg2.connect(**config) as conn:
            print('Connected to the PostgreSQL server.')
            query = "CREATE TABLE qrcodes2 if not exist (id SERIAL PRIMARY KEY, uuid VARCHAR(36), qrdata VARCHAR(500));"
            with conn.cursor() as cur:
                cur.execute(query)
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

#TODO make function work
def save_qr_data(**data):
    pass
    
    
    
    

# If this module is run directly, load the configuration and connect to the database
if __name__ == '__main__':
    config = load_config()
    connect(config)
    
    
