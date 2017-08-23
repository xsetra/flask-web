# -*- coding: utf-8 -*-

from flask import Flask, render_template, redirect, url_for, request, make_response

application = Flask(__name__)

@application.route('/')
def index():
    return render_template('_7_index.html')

@application.route('/setcookie', methods=['GET', 'POST'])
def setcookie():
    if request.method == 'POST':
        username = request.form['username']
        resp = make_response("<a href='"+ url_for('getcookie') +"'>Click</a>")
        resp.set_cookie('userID', username)

        return resp

@application.route('/getcookie')
def getcookie():
    username = request.cookies.get('userID')
    return "<h1>Welcome, {}</h1>".format(username)


if __name__ == "__main__":
    application.run('localhost', 5000, debug=1)
