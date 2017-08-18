# -*- coding: utf-8 -*-

from flask import Flask, url_for, render_template, redirect, request

"""
Important Attributes of REQUEST object
    --> method      : Show request method, GET, POST...
    --> Form        : Show POST data, Form['username'] (dict)
    --> args        : Show query string, ?username
    --> Cookies     : Cookie data. (dict)
    --> files       : Multipart form data.
"""

app = Flask(__name__)

@app.route('/sign')
def sign():
    return render_template('_6_request_form.html')

@app.route('/sign/up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':

if __name__ == '__main__':
    app.run('localhost', 5000, debug=1)