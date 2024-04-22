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

cur2 = conn.cursor()

sql2 = "SELECT * FROM cities ORDER BY pop DESC"

cur2.execute( sql2 )
row2 = cur2.fetchone()

print("Largest population:", row2[0])

cur3 = conn.cursor()

sql3 = "SELECT * FROM cities WHERE states='Minnesota' ORDER BY pop ASC"

cur3.execute( sql3 )
row3 = cur3.fetchone()

print("city in Minnesota with the least population:", row3[0])