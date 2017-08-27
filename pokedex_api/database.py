# -*- coding: utf-8 -*-

import rethinkdb as r


class Database(object):
    def __init__(self):
        self.conn = r.connect(db='pokedex')
        self.table = None

    def set_table(self, table):
        self.table = self.conn.table(table)

    def get_pokemon(self, number=None):
        """
        Get pokemon(s) object from database
        Args:
            number (int): Pokemon number

        Returns:
            dict: Rethinkdb status object
        """
        pass

    def insert_pokemon(self, pokemon):
        """
        Insert pokemon to database.
        Args:
            pokemon (dict): Pokemon

        Returns:
            dict: Status of process
        """
        self.set_table('pokemon')
        return self.table.insert(pokemon)
