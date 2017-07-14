from flask import flash, render_template, request, session, redirect, url_for, make_response, got_request_exception
from app import app
from datetime import datetime
from app.models.user import User
from app.models.bucketlist import BucketList
from app.models.activity import Activity
from app.models.sharing_pool import SharingPool

users = {}
sharing_pool = SharingPool()
current_bucketlists = {}
current_activities = {}

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template("login.html")
    else:
        current_user = users[session.get('username')]
        age = datetime.now().date().year - current_user.birthday.year
        shares = len(sharing_pool.bucketlists)
        total_bucketlists = current_bucketlists[current_user.username]
        for username1, bucketlist_list4 in sharing_pool.bucketlists.items():
            if not username1 == current_user.username:
                exists2 = False
                for bucketlist5 in bucketlist_list4:
                    for bucketlist6 in current_bucketlists[current_user.username]:
                        if bucketlist5.title == bucketlist6.title:
                            exists2 = True
                            break
                    if not exists2:
                        total_bucketlists.append(bucketlist5)

        current_bucketlists[current_user.username] = total_bucketlists
        return render_template("home.html", bucketlists=current_bucketlists[current_user.username],
                               sharing_pool_bucketlists=sharing_pool.bucketlists,
                               shares=shares, age=str(age), activities=current_activities)


@app.route('/login', methods=['POST'])
def login():
    if users and request.form['username'] in users.keys():
        user = users[request.form['username']]
        if user.password == request.form['password']:
            session['username'] = user.username
            session['first_name'] = user.first_name
            session['logged_in'] = True
    else:
        flash('Invalid username or password!')
    return redirect(url_for('home'))


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
        current_bucketlists[new_user.username] = []
        if new_user.username in users.keys():
            session['username'] = new_user.username
            session['first_name'] = new_user.first_name
            session['logged_in'] = True
            return redirect(url_for('home'))
    else:
        return sign_up_page()



@app.route("/add_bucketlist", methods=['POST'])
def add_bucketlist():
    title = request.form['title']
    new_bucketlist = BucketList(title)
    bucketlist_list = [new_bucketlist]
    if current_bucketlists[session.get('username')]:
        bucketlist_list = current_bucketlists[session.get('username')]
        exists = False
        for bucketlist0 in bucketlist_list:
            if bucketlist0.title == new_bucketlist.title:
                exists = True
                break
        if not exists:
            bucketlist_list.append(new_bucketlist)
            current_activities[new_bucketlist.title] = []
    current_bucketlists[session.get('username')] = bucketlist_list
    return redirect(url_for('home'))


@app.route("/edit_bucketlist", methods=['POST'])
def edit_bucketlist():
    old_title = request.form['old_title']
    new_title = request.form['new_title']
    bucketlist_list1 = current_bucketlists[session.get('username')]
    for bucketlist1 in bucketlist_list1:
        if old_title == bucketlist1.title:
            bucketlist1.change_title(new_title)
            break
    return redirect(url_for('home'))

@app.route("/remove_bucketlist/<title>")
def remove_bucketlist(title):
    if session.get('logged_in'):
        bucketlist_list2 = current_bucketlists[session.get('username')]
        for bucketlist2 in bucketlist_list2:
            if title == bucketlist2.title:
                bucketlist_list2.remove(bucketlist2)
                break
    current_bucketlists[session.get('username')] = bucketlist_list2
    return redirect(url_for('home'))

@app.route("/share_bucketlist/<title>")
def share_bucketlist(title):
    if session.get('logged_in'):
        bucketlist_list3 = current_bucketlists[session.get('username')]
        for bucketlist3 in bucketlist_list3:
            if title == bucketlist3.title:
                if session.get('username') in sharing_pool.bucketlists.keys():
                    exists1 = False
                    for bucketlist4 in sharing_pool.bucketlists[session.get('username')]:
                        if bucketlist3.title == bucketlist4.title:
                            exists1 = True
                            break
                    if not exists1:
                        sharing_pool.add_bucket(session.get('username'), bucketlist3)
                else:
                    sharing_pool.add_bucket(session.get('username'), bucketlist3)
                    break
    return redirect(url_for('home'))


@app.route("/add_bucket_activity", methods=['POST'])
def add_bucket_activity():
    name = request.form['name']
    bucket_title = request.form['bucket_title']
    target_age = request.form['target_age']
    new_activity = Activity(name, target_age)
    bucketlist_list7 = current_bucketlists[session.get('username')]
    for bucketlist7 in bucketlist_list7:
        if bucket_title == bucketlist7.title:
            activity_list = [new_activity]
            if current_activities:
                if bucket_title in current_activities.keys():
                    activity_list = current_activities[bucket_title]
                    exists3 = False
                    for activity1 in activity_list:
                        if activity1.name == new_activity.name:
                            exists3 = True
                            break
                    if not exists3:
                        activity_list.append(new_activity)
                        break
            current_activities[bucket_title] = activity_list
            break
    return redirect(url_for('home'))


