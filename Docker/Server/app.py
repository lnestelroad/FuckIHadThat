from flask import Flask, render_template, request
import psycopg2 as psql
import json

app = Flask(__name__)

# def connect():
#     conn = psql.connect(host="db",database="fuckihadthat", user="FIHT", password="FIHT")
#     cur = conn.cursor()

#     cur.execute('SELECT version()')
#     print('PostgreSQL database version: ', cur.fetchall())


@app.route('/')
def hello():
    # connect()
    return render_template("index.html")

@app.route('/data/', methods=['GET'])
def db():
    if request.method == 'GET':
        conn = psql.connect(host="db",database="fuckihadthat", user="FIHT", password="FIHT")

        cur = conn.cursor()
        cur.execute("SELECT * FROM cans")    
        
        rows = cur.fetchall()
        data = []
        for row in rows:
            data.append(dict(row))
        
        conn.close()

    return render_template("index.html", data=data)

# @app.route('/input/', methods=['GET','POST'])
# def input():
#     first = request.form['first']
#     last = request.form['last']
#     age = request.form['age']
#     major = request.form['major']

#     conn = sql.connect("testData.db")
#     conn.row_factory = sql.Row 

#     cur = conn.cursor()
#     cur.execute("INSERT INTO people (first, last, age, major) VALUES (?,?,?,?)",(first, last, age, major))    
#     conn.commit()

#     conn.close()

#     return render_template("index.html", )

if __name__ == '__main__':
    app.run(debug=True)