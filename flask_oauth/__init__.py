# -*- coding: utf-8 -*-

from flask import Flask, render_template, redirect, url_for
from flask_restful import Resource, Api

application = Flask(__name__)
api = Api(application)


class AccountManagement(Resource):
    def get(self):
        return render_template()


if __name__ == '__main__':
    application.run('localhost', 5000, debug=True)