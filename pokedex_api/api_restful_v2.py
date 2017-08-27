# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Api, Resource, reqparse
from database import Database


class Pokemon(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('number', required=False, type=int, location='args')

        args = parser.parse_args()
        number = args.get('number', None)

        if number is not None:



app = Flask(__name__)
api = Api(app)

api.add_resource(Pokemon, '/api/v2/pokemon', endpoint='api.v2.pokemon')