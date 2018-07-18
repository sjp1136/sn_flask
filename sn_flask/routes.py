from flask import render_template, url_for, flash, redirect
from sn_flask import app
from sn_flask.models import User, Post
from sn_flask.forms import RegistrationForm, LoginForm


#######################
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
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(format('Account created for {form.username.data}!'), 'success')
        return redirect(url_for('home'))
    else:
        flash(format(
            'Account registration for {form.username.data} unsuccessful!'), 'danger')

    return render_template('register.html', title="Register", form=form)


@app.route("/login", methods=["GET", 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login was unsuccessful. Please check username and password.', 'danger')
    return render_template('login.html', title="Login", form=form)
