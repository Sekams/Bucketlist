from flask import render_template

from app import app

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/signup')
def sign_up():
    return render_template("sign_up.html")
