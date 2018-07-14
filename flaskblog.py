from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
######################
# TO GET SECRET_KEY #
# import secrets
# secrets.token_hex(16)
#######################

app.config['SECRET_KEY'] = "227aa38d1a26516c7289032c5db9cf97"

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


if __name__ == '__main__':
    app.run(debug=True)
