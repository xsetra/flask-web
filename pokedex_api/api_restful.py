from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)


pokedex = [{'number': 14, 'name': 'Kakuna'},
           {'number': 16, 'name': 'Pidgey'},
           {'number': 50, 'name': 'Diglett'}]


class Pokemon(Resource):
    def get(self):
        return pokedex

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, location='json')
        parser.add_argument('number', type=str, required=True, location='json')

        args = parser.parse_args(strict=True)
        pokemon = {'name': args['name'], 'number': args['number']}

        if pokemon in pokedex:
            return {'status': 'Pokemon is exists, nothing to do'}

        pokedex.append(pokemon)
        return pokedex[-1]

api.add_resource(Pokemon, '/api/v1/pokemon')


if __name__ == '__main__':
    app.run('localhost', 5000, debug=True)
