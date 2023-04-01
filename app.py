from flask import Flask, redirect, render_template, request, session
from os import getenv
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()
app.secret_key=getenv("SECRET_KEY")