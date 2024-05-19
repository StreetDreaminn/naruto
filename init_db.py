import psycopg2 

conn = psycopg2.connect(
    database="postgres",
    host="locahost",
    user="postgres",
    password="test123",
    port="5432")

cur = conn.cursor()
cur.close()
conn.close()