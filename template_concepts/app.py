# -*- coding: utf-8 -*-

from flask.ext.script import Manager
from flask import Flask, render_template

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
    print(app.url_map)
    return render_template('index.html')


if __name__ == "__main__":
    manager.run()