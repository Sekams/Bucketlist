from flask import flash, render_template, request, session
from app import app
from datetime import datetime
from app.models.user import User

users = {}

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template("login.html")
    else:
        return render_template("home.html")


@app.route('/login', methods=['POST'])
def login():
    if request.form['username'] in users.keys() and users[request.form['username']] == request.form['password']:
        session['logged_in'] = True
    else:
        flash('Invalid username or password!')
    return home()


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()


@app.route('/signup')
def sign_up_page():
    return render_template("sign_up.html")


@app.route('/signup', methods=['POST'])
def sign_up():
    the_form = request.form
    if the_form:
        last_name = ""
        name = the_form['name']
        names = name.split()
        if len(names) > 1:
            last_name = names[len(names)-1]
        first_name = names[0]
        new_user = User(
            username=the_form['username'],
            password=the_form['password'],
            first_name=first_name,
            last_name=last_name,
            birthday=datetime.strptime(str(the_form['birthday']), '%Y-%m-%d')
        )
        users[new_user.username] = new_user
        if new_user.username in users.keys():
            session['logged_in'] = True
            return home()
    else:
        return sign_up_page()