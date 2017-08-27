# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify, json, abort

app = Flask(__name__)
pokedex = [{'number': 14, 'name': 'Kakuna'},
           {'number': 16, 'name': 'Pidgey'},
           {'number': 50, 'name': 'Diglett'}]


@app.route('/api/v1/pokemon', methods=['GET', 'POST'])
def pokemon():
    if request.method == 'GET':
        response = pokedex

    else: # POST
        if request.content_type != 'application/json':
            response = {'400': 'Bad Request, The content-type must be application/json'}

        else:
            try:
                new_pokemon = json.load(request.data)
            except ValueError:
                return jsonify({'400': 'Bad Request, JSON format is not correct'})
            pokedex.append({'name': new_pokemon['name'],
                            'number': new_pokemon['number']})
            response = pokedex[-1]

    return jsonify(response)

if __name__ == '__main__':
    app.run('localhost', 5000, debug=True)
