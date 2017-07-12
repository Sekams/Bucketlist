from flask import Flask, flash, redirect, render_template, request, session, abort
from app import app
from app.models.user import User

current_user = User()

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template("login.html")
    else:
        return render_template("home.html")


@app.route('/login', methods=['POST'])
def login():
    if request.form['password'] == 'duff' and request.form['username'] == 'homer':
        session['logged_in'] = True
    else:
        flash('Invalid username or password!')
    return home()


@app.route('/signup')
def sign_up():
    return render_template("sign_up.html")
