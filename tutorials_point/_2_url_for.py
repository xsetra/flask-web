# -*- coding: utf-8 -*-

from flask import Flask, redirect, url_for

app = Flask(__name__)

def hello_admin():
    return "<h1>Hello Admin</h1>"

def hello_guest(guest_name):
    return "<h1>Hello Guest, {}</h1>".format(guest_name)

def hello_user(user_name):
    if user_name == 'admin':
        return redirect(url_for('hello_admin'), code=302)
    else:
        return redirect(url_for('hello_guest', guest_name=user_name), code=302)

app.add_url_rule('/admin', view_func=hello_admin)
app.add_url_rule('/guest/<guest_name>', view_func=hello_guest)
app.add_url_rule('/user/<user_name>', view_func=hello_user)


if __name__ == "__main__":
    app.run('localhost', 5000, debug=1)