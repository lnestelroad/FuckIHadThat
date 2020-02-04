from flask import Flask, render_template, request
import psycopg2 as psql
import json
import logging
import database_interface

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html", data=data)

@app.route('/data/', methods=['GET'])
def db():
    return render_template("index.html", data=data)

if __name__ == '__main__':
    app.run(debug=True)