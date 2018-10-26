import psycopg2
import os

url = "dbname='postgres' host='localhost' port='5432'user='postgres'password='password'"
conn = psycopg2.connect(url)
cur = conn.cursor()
