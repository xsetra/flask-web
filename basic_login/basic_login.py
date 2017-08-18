# -*- coding: utf-8 -*-

from flask import Flask, render_template, redirect, url_for, request

application = Flask(__name__)


@application.route('/')
def index():
    return render_template("index.html")


@application.route('/register')
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']


@application.route('/login')
def login():
    pass


if __name__ == "__main__":
    application.run('localhost', 5000, debug=1)
