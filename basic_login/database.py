# -*- coding: utf-8 -*-

import pymysql
import hashlib


class Database(object):
    def __init__(self, hostname, username, password, database):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.db_name = database

        self.conn = None
        self.cursor = None
        self.connect()

    def connect(self):
        try:
            self.conn = pymysql.connect(self.hostname,
                                      self.username,
                                      self.password,
                                      self.db_name)
            self.cursor = self.conn.cursor()
        except Exception as e:
            raise e

    def disconnect(self):
        try:
            self.conn.close()
        except Exception as e:
            raise e

    @staticmethod
    def hashing(password):
        return hashlib.sha512(password.encode()).hexdigest()

    def exec_sql(self, sql):
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            return True
        except Exception as e:
            self.conn.rollback()
            raise e

    def add_user(self, username, password):
        sql = "INSERT INTO users(username, password) VALUES('{}', '{}')".format(username, self.hashing(password))
        return self.exec_sql(sql)

    def check_user(self, username, password):
        sql = "SELECT * FROM users WHERE username='{}' and password='{}'".format(username, self.hashing(password))
        if self.exec_sql(sql):
            res = self.cursor.fetchone()
            if res:
                return True
            else:
                return "Username or password is wrong!"
