# -*- coding: utf-8 -*-

from flask import Flask


# Create Flask application object. That requires an arg for resolve the path.
app = Flask(__name__)


# Create a view function for root path. Decorate a python function with app.route()
@app.route('/')
def index():
    # It's a view function.
    return "<h2>Hello, FLASK!</h2>", 200
    # 200 is a status_code of response. It's not require


@app.route('/user/<name>')
def get_user(name):
    return "Welcome, {}".format(name), 200


def list_users():
    return "LIST OF USERS", 200
app.add_url_rule(rule='/user', endpoint='list_users', view_func=list_users)

# Run Flask web server. Debug mode on, port 8000.
if __name__ == '__main__':
    app.run(port=8000, debug=1)

# You can test typing that, "curl -X GET localhost:8000"
