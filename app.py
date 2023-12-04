from flask import Flask, render_template, request
from db.models import *

app = Flask(__name__)

@app.route("/")
def mainPage():
    return render_template("index.html")

@app.route("/products", methods=['GET', 'POST'])
def productsPage():
    if request.method == "GET":
        return render_template("products.html", products=getALLProducts())
    elif request.method == "POST":
        min = request.form["min"]
        max = request.form["max"]
        return render_template("products.html", products=getSomeProducts(min, max))

@app.route("/contacts")
def contactsPage():
    return render_template("contacts.html")


app.run(debug=True)