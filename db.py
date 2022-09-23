import psycopg2

conn = psycopg2.connect("dbname='usermgt' user='johnipson' host='localhost'")
cursor = conn.cursor()

def create_all():
  print("Creating tables...")
  cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users (
        user_id SERIAL PRIMARY KEY,
        first_name VARCHAR NOT NULL,
        last_name VARCHAR,
        email VARCHAR NOT NULL UNIQUE,
        phone VARCHAR,
        city VARCHAR,
        state VARCHAR,
        org_id int,
        active smallint
    );
  """)
  cursor.execute("""
    CREATE TABLE IF NOT EXISTS Organizations (
        org_id SERIAL PRIMARY KEY,
        name VARCHAR NOT NULL,
        phone VARCHAR,
        city VARCHAR,
        state VARCHAR,
        active smallint
    );
  """)
  conn.commit()