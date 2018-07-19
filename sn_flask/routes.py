from flask import render_template, url_for, flash, redirect, request
from sn_flask import app, db, bcrypt
from sn_flask.models import User, Post
from sn_flask.forms import RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required

#######################
# To Create Passowrd #

# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt()
# hashed_pwd= bcrypt.generate_password_hash('testing').decode('utf-8')
# bcrypt.check_password_hash(hashed_pwd, 'testing')

# To Create Databases #
# from sn_flask import db
# from sn_flask.models import User, Post
# db.create_all()
# user_1 = User(username = 'Sung Joon', email = 'sjp@gmail.com', password = 'password')
# db.session.add(user_1)
# user_2 = User(username = 'Joshua Kim', email = 'joshua@gmail.com', password='password')
# db.session.add(user_2)
# db.session.commit()

# User.query.all()
# User.query.first()
# user = User.query.filter_by(username = 'Sung Joon').all()
# user = User.query.get(1) #gets user with id of 1
# post_1 = Post(title = "Blog 1", content = "First", user_id = user.id)
# db.session.add(post_1)
# db.session.commit()
# user.posts

# post = Post.query.first()
# post.user_id

# post.author

# db.drop_all()
#######################


posts = [
    {
        'author': "Sung Joon Park",
        'title': 'My First Post!',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': "Crazy George",
        'title': 'My Second Post!',
        'content': 'First Second content',
        'date_posted': 'April 21, 2018'
    }


]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title="About")


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = User(username=form.username.data,
                    email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in.', 'success')
        return redirect(url_for('login'))
    else:
        flash(format(
            'Account registration for {form.username.data} unsuccessful!'), 'danger')

    return render_template('register.html', title="Register", form=form)


@app.route("/login", methods=["GET", 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
            # ternary conditional
        else:
            flash('Login was unsuccessful. Please check email and password.', 'danger')
    return render_template('login.html', title="Login", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')
