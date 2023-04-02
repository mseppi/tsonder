from app import app
from flask import Flask, redirect, render_template, request, session
from userdata import login, register
from os import urandom

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login_app():
    if request.method=="POST":
        username = request.form["username"]
        password = request.form["password"]
        if login(username, password):
            session["user_name"] = username
            session["csrf_token"] = urandom(16).hex()
            return redirect('/')
        else:
            return "Väärä käyttäjätunnus tai salasana"
    return render_template("login.html")
	    

@app.route("/logout")
def logout():
	del session["username"]
	return redirect("/")

@app.route("/register", methods=["POST"])
def register_app():
    username = request.form["username"]
    password = request.form["password"]
    role = request.form.get('role')
    if username and password and role:
        result=register(username, password, role)
        if result:
            return "Käyttäjä rekisteröity"
    return "Rekisteröinti epäonnistui"