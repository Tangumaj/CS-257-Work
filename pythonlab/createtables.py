# We use the psycopg2 library to help us connec to the Postgres SQL database
# This library is already installed on stearns.mathcs.carleton.edu
import psycopg2


conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="tangumaj",
    user="tangumaj",
    password="ardi363puppy")
    
cur = conn.cursor()

sql = """DROP TABLE IF EXISTS cities;
CREATE TABLE cities (
  city text,
  states text,
  pop real,
  lat real,
  lon real
);"""
sql1 = """DROP TABLE IF EXISTS states;
CREATE TABLE states (
    code text,
    state text,
    pop real
);"""
    
cur.execute( sql )
cur.execute( sql1 )
