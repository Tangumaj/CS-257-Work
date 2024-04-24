import flask
import psycopg2

app = flask.Flask(__name__)

#
@app.route('/hello')
def my_function():
    return "Hello World!"

@app.route('/display/<word1>/<word2>')
def my_display(word1, word2):
    the_string = "The words are: " + word1 + " and " + word2;
    return the_string

@app.route('/color/<word1>')
def my_color(word1):
    return '<h1 style="color:Yellow">' + word1 + '</h1>'

@app.route('/add/<num1>/<num2>')
def my_add(num1, num2):
    a = int(num1)
    b = int(num2)
    add = a + b
    num = str(add)
    return "The result is " + num

@app.route('/pop/<abbrev>')
def my_pop(abbrev):
    
    conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="tangumaj",
    user="tangumaj",
    password="ardi363puppy")
    
    cur = conn.cursor()

    sql = "SELECT * FROM states WHERE states=%s"
    
    cur.execute( sql, [abbrev] )
    
    row = cur.fetchone()
    
    if row == None:
        return "Not found, please look for another city"
    else:
        return "The population is: " + str(row[2])


if __name__ == '__main__':
    my_port = 5227
    app.run(host='0.0.0.0', port = my_port) 
