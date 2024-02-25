#!/usr/bin/env python 
"""Contains the database connection and all communication with the database"""
import psycopg2

params = {"host" :"localhost",
          "port" : 5432,
        "database" : "qrcodes",
        "user" :"postgres",
        "password": "****"}


def connect():
    """
    Connects to a PostgreSQL database using the provided configuration.

    Prints a message indicating whether the connection was successful.
    Returns the database connection object on success."""
    try:
        # connecting to the PostgreSQL server        
        with psycopg2.connect(**params) as conn:
            print('Connected to the PostgreSQL server.')
            conn.execute("""
            CREATE TABLE IF NOT EXISTS qrcode(
            id BIGSERIAL PRIMARY KEY,
            employee_name VARCHAR,
            personal_website VARCHAR,
            phone_number INT,
            email_address VARCHAR,
            qr_image VARCHAR) 
            """)
            # TODO qr_image from VARCHAR BYTEA
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
