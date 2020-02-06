from flask import Flask, render_template, request
import psycopg2 as psql
import json
import logging
import database_interface

app = Flask(__name__)

@app.route('/')
def hello():
    db = database_interface.Database()
    db.connectToDatabase()

    food = db.getAllFood()
    return render_template("index.html", Food=food)

@app.route('/input/', methods=['POST'])
def db():

    if request.method == "POST":
        food_name = request.form['food_name']
        food_quantity = request.form['food_quantity']
        expire = request.form['exp_date']
        food_type = request.form['food_type']

        db = database_interface.Database()
        db.connectToDatabase()

        db.addFood(food_name, int(food_quantity), expire, food_type)
        db.commitChanges()

        food = db.getAllFood()

    return render_template("index.html", Food=food)

if __name__ == '__main__':
    app.run(debug=True)