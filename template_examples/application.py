from flask import Flask, render_template, flash, request, redirect, url_for, session
from passlib.hash import sha256_crypt
import gc

from mysql import Database
from forms import RegistrationForm


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('main.html')


@app.route('/dashboard/')
def dashboard():
    flash('TEST 1')
    flash('TEST MESSAGE 2')
    flash('TEST MESSAGE EXAMPLES 3')
    return render_template('dashboard.html', TOP_CONTENT=content())


@app.route('/slashboard/')
def slashboard():
    try:
        return render_template('dashboard.html', TOP_CONTENT=boom )
    except Exception as e:
        return render_template('500.html', error=str(e))


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    try:
        form = RegistrationForm(request.form)

        if request.method == "POST" and form.validate():
            username = form.username.data
            email = form.email.data
            password = sha256_crypt.encrypt(str(form.password.data))

            db = Database()
            if db.is_user_exists(username):
                flash("This username is already taken. Please choose another username.")
                return render_template('register.html')


    except Exception as e:
        pass


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    error = ''
    try:
        if request.method == "POST":

            attempted_username = request.form['username']
            attempted_password = request.form['password']

            if attempted_username == "admin" and attempted_password == "password":
                return redirect(url_for('dashboard'))

            else:
                error = "Invalid credentials. Try Again."

        return render_template("login.html", error=error)

    except Exception as e:
        # flash(e)
        return render_template("login.html", error=error)


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')


def content():
    CONTENT = {"Basics":[["Introduction to Python","/intro/"],
                            ["Print functions and Strings","/print/"],
                            ],
                  "WebDev":[]}
    return CONTENT

if __name__ == '__main__':
    app.secret_key = "secret_key_first"
    app.run(debug=1)
