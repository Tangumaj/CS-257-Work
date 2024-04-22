import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="tangumaj",
    user="tangumaj",
    password="ardi363puppy")
    
cur = conn.cursor()

sql = "SELECT * FROM cities WHERE city='Northfield'"
    
cur.execute( sql )

row = cur.fetchone()

if row == None:
    print("Not found, please look for another city")
else:
    print( "Lat: ", row[3] ) 
    print( "Lon: ", row[4] ) 

sql2 = "SELECT pop FROM cities ORDER BY DESC"

cur.execute( sql2 )
row2 = cur.fetchone()

if row2 == None:
    print("Error")
else:
    print(row[0])