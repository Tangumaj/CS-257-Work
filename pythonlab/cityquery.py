import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="tangumaj",
    user="tangumaj",
    password="ardi363puppy")
    
cur = conn.cursor()

sql = "SELECT * FROM cities WHERE city='Marysville'"
    
cur.execute( sql )

row = cur.fetchone()

for i in row:
    if i == 3:
        print(i)
    elif i == 4:
        print(i)