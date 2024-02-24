#!/usr/bin/env python 
"""Contains the database connection and all communication with the database"""
import psycopg2

conn = psycopg2.connect(host = "localhost",database ="postgresql", user="postgres", password="HisGrace@4", port="5432")