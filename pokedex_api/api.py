# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify, json

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
            print('Apo')

if __name__ == '__main__':
    app.run('localhost', 5000, debug=True)
