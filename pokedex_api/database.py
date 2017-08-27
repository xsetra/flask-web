# -*- coding: utf-8 -*-

import rethinkdb as r


class Database(object):
    def __init__(self):
        self.conn = r.connect(db='pokedex')
        self.db = r.db(self.conn.db)

    def get_pokemon(self, number=None):
        """
        Get pokemon(s) object from database
        Args:
            number (int): Pokemon number

        Returns:
            list of dict: Pokemon object's list
        """
        if number is not None:
            return self.db.table('pokemon').filter({'number': number}).run(self.conn)
        return self.db.table('pokemon').run(self.conn)

    def insert_pokemon(self, pokemon):
        """
        Insert pokemon to database.
        Args:
            pokemon (dict): Pokemon

        Returns:
            dict: Status of process
        """
        db_pokemon = self.get_pokemon(pokemon['number'])
        if db_pokemon.threshold == 0:
            return self.db.table('pokemon').insert(pokemon).run(self.conn)
        return {"400": "Pokemon exists, dont added."}
