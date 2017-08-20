# -*- coding: utf-8 -*-

from flask import Flask, render_template, redirect, url_for, request
from database import Database
import os

HOST = os.environ.get('hostname')
USER = os.environ.get('username')
PASS = os.environ.get('password')
DB = os.environ.get('db_name')

application = Flask(__name__)
db = Database(HOST, USER, PASS, DB)


@application.route('/')
def index():
    return render_template("index.html")


@application.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if db.add_user(username, password):
            return redirect(url_for('index'), code=302)
        else:
            return render_template('register.html', error="Something happened!")
    else:
        return render_template('register.html')


@application.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if db.check_user(username, password):
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error="Username or password is wrong!")
    else:
        return render_template('login.html')


if __name__ == "__main__":
    application.run('localhost', 5000, debug=1)
