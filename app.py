from flask import Flask, render_template, request, session, redirect
from db.models import *

app = Flask(__name__)
app.secret_key = "secret key"

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

@app.route("/admin")
def adminPage():
    if "login" not in session:
        return redirect("/admin/login")
    return render_template("admin.html", login=session["login"])
    
@app.route("/admin/login", methods=["GET", "POST"])
def adminLoginPage():
    if request.method == "GET":
        return render_template("adminLogin.html")
    elif request.method == "POST":
        login = request.form["login"]
        password = request.form["password"]

        user = getUser(login, password)

        if user:
            session["login"] = user[1]
            return redirect("/admin")
        else:
            return render_template("adminLogin.html", error="Логин или пароль введены неправильно")



app.run(debug=True)