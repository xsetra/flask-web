import MySQLdb
import os


class Database:
    __conn_instance = None

    def __init__(self):
        self.get_instance()
        self.conn = self.__conn_instance

    @classmethod
    def get_instance(cls):
        if cls.__conn_instance is None:
            cls.__init_instance()

        return cls.__conn_instance

    @classmethod
    def __init_instance(cls):
        host = os.environ.get('DB_HOST')
        user = os.environ.get('DB_USER')
        pasw = os.environ.get('DB_PASS')
        db_name = os.environ.get('DB_NAME')

        cls.__conn_instance = MySQLdb.connect(host=host,
                                            user=user,
                                            passwd=pasw,
                                            db=db_name)