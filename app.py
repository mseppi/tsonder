from flask import Flask, redirect, render_template, request, session
from os import getenv
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()
app.secret_key=getenv("SECRET_KEY")

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
	username=request.form["username"]
	password=request.form["password"]
	session["username"]=username
	return redirect("/")

@app.route("/logout")
def logout():
	del session["username"]
	return redirect("/")
