# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Api, Resource, reqparse
from database import Database


class Pokemon(Resource):
    def __init__(self):
        super(Pokemon, self).__init__()
        self.db = Database()

    @staticmethod
    def parse_pokemon_args():
        root_parser = reqparse.RequestParser()

        root_parser.add_argument('name', required=True, type=str, location='json', help='Have to send name.')
        root_parser.add_argument('number', required=True, type=int, location='json', help='Have to send number.')
        root_parser.add_argument('weaknesses', required=True, type=list, location='json')

        root_args = root_parser.parse_args(strict=True)
        return root_args

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('number', required=False, type=int, location='args')

        args = parser.parse_args()
        number = args.get('number', None)

        pokemons = self.db.get_pokemon(number)
        resp = []
        for pokemon in pokemons:
            resp.append(pokemon)

        return resp

    def post(self):
        args = self.parse_pokemon_args()

        new_pokemon = {
            'name': args['name'],
            'number': args['number'],
            'weaknesses': args['weaknesses']
        }
        return self.db.insert_pokemon(new_pokemon)

app = Flask(__name__)
api = Api(app)

api.add_resource(Pokemon, '/api/v2/pokemon', endpoint='api.v2.pokemon')

if __name__ == '__main__':
    app.run('localhost', 5000, debug=True)
