# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Resource, Api, fields, marshal_with

app = Flask(__name__)
api = Api(app)

todos = {
    'todo1': {'name':'A', 'version':1, 'hidden_key':'A1'},
    'todo2': {'name':'B', 'version':2, 'hidden_key':'B2'}
}

todo_fields = {
    "todo": fields.String(attribute='name'),
    "version": fields.Integer
}


class Todo(Resource):
    @marshal_with(todo_fields)
    def get(self, todo_id):
        return todos[todo_id]

api.add_resource(Todo, '/todo/<todo_id>')

if __name__ == '__main__':
    app.run('localhost', 5000, debug=True)