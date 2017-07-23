# -*- coding: utf-8 -*-

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    return "Index Page", 200


@app.route('/request/info')
def request_info():
    method = request.method
    user_agent = request.headers.get('User-Agent')
    accept_type = request.headers.get('Accept')
    accept_language = request.headers.get('Accept-Language')
    accept_encoding = request.headers.get('Accept-Encoding')

    return "Request Information : <br>" \
           "{} - {} - {} - {} - {}".format(method, user_agent, accept_type, accept_language, accept_encoding), 200


if __name__ == "__main__":
    app.run(port=8000, debug=1)
