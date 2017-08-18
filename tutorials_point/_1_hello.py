# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)


@app.route('/deneme')
def deneme():
    return "Deneme"


@app.route('/blog/<int:post_id>')
def show_post(post_id):
    return "The blog number is {}".format(post_id)


@app.route('/')
def hello():
    return "Hello World"


def hello_world(name):
    return "Hello World Page " + str(name)
app.add_url_rule('/hello/<name>', 'Hello Page', hello_world)


if __name__ == "__main__":
    app.run('localhost', 5000, debug=1)