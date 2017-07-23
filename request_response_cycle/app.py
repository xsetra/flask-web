# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import abort

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


@app.route('/make/response')
def get_response():
    resp = make_response("<h1>Response object produced</h1>", 200)
    resp.set_cookie('resp', '1')
    return resp


@app.route('/route/me/<address>')
def route_that(address):
    resp = make_response('', 302, {'Location': address})
    return resp


@app.route('/redirect')
def redirect_that():
    return redirect('/make/response', 302)


@app.route('/404')
def _404():
    abort(make_response('404 Page. There is nothing.'))

if __name__ == "__main__":
    app.run(port=8000, debug=1)
