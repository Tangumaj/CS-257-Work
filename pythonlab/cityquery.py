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

cur4 = conn.cursor()

sql4 = "SELECT * FROM cities ORDER BY lat ASC"
sql5 = "SELECT * FROM cities ORDER BY lat DESC"
sql6 = "SELECT * FROM cities ORDER BY lon ASC"
sql7 = "SELECT * FROM cities ORDER BY lon DESC"

cur4.execute( sql4 )
row4 = cur4.fetchone()

cur4.execute( sql5 )
row5 = cur4.fetchone()

cur4.execute( sql6 )
row6 = cur4.fetchone()

cur4.execute( sql7 )
row7 = cur4.fetchone()


print("Eastmost City:", row4[0])
print("Westmost City:", row5[0])
print("Southmost City:", row6[0])
print("Northmost City:", row7[0])

val = input("please enter a state: ")
cur5 = conn.cursor()

if len(val) == 2:
    sql8 = "SELECT *FROM states WHERE code = %s"
    state_abb1 = val
    cur5.execute(sql8, [state_abb1])
    row8 = cur5.fetchone()
    state = row8[1]

    sql9 = "SELECT * FROM cities WHERE state = %s"

    cur5.execute(sql9, [state])
    cities_from_state = cur5.fetchall()

    total = 0 
    for x in cities_from_state:
        total = total + int(x[2])

    print(total)
else:
    sql10 = "SELECT * FROM cities WHERE state = %s"
    state_abb1 = val
    cur5.execute(sql10, [state_abb1])
    cities_from_state = cur5.fetchall()

    total = 0 
    for x in cities_from_state:
        total = total + int(x[2])

    print(total)
