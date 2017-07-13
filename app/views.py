from flask import flash, render_template, request, session, redirect, url_for
from app import app
from datetime import datetime
from app.models.user import User
from app.models.bucketlist import BucketList
from app.models.activity import Activity

users = {}

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template("login.html")
    else:
        current_user = users[session.get('username')]
        return render_template("home.html", bucketlists=current_user.bucketlists)


@app.route('/login', methods=['POST'])
def login():
    if users and request.form['username'] in users.keys():
        user = users[request.form['username']]
        if user.password == request.form['password']:
            session['username'] = user.username
            session['logged_in'] = True
    else:
        flash('Invalid username or password!')
    return home()


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return redirect(url_for('home'))


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
            session['username'] = new_user.username
            session['logged_in'] = True
            return redirect(url_for('home'))
    else:
        return sign_up_page()



@app.route("/add_bucketlist", methods=['POST'])
def add_bucketlist():
    title = request.form['title']
    new_bucketlist = BucketList(title)
    current_user = users[session.get('username')]
    current_user.create_bucketlist(new_bucketlist)
    return redirect(url_for('home'))


@app.route("/edit_bucketlist", methods=['POST'])
def edit_bucketlist():
    old_title = request.form['old_title']
    new_title = request.form['new_title']
    current_user = users[session.get('username')]
    bucketlist = current_user.bucketlists[old_title]
    bucketlist.change_title(new_title)
    return redirect(url_for('home'))

@app.route("/remove_bucketlist")
def remove_bucketlist():
    title = request.form['title']
    current_user = users[session.get('username')]
    if current_user.bucketlists[title]:
        bucketlist = BucketList(title)
        current_user.remove_bucketlist(bucketlist)
    return redirect(url_for('home'))


# @app.route("/add_activity", methods=['POST'])
# def add_bucketlist():
#     name = request.form['name']
#     new_activity = Activity(name)
#     current_user = users[session.get('username')]
#     current_user.create_bucketlist(new_bucketlist)
#     return redirect(url_for('home'))