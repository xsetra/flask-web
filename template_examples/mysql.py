import MySQLdb
import os


class Database:
    __conn_instance = None

    def __init__(self):
        self.get_instance()
        self.conn = self.__conn_instance
        self.cursor = self.conn.cursor()

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

    def strings_escape(self, *args):
        for arg in args:
            arg = MySQLdb.escape_string(arg)

    def is_user_exists(self, username):
        """
        Check the username on the database. If exists, return True, or not False
        Args:
            username: <str>

        Returns: If user exists, return True. <bool>
        """

        # username = MySQLdb.escape_string(username)
        query = "SELECT * FROM users WHERE username={}"

        row = self.cursor.execute(query, (username))
        if int(row) != 0:
            return True
        else:
            return False

    def insert_user(self, username, password, email):
        """
        Insert information of user.
        Args:
            username: <str>
            password: <str>
            email: <str>

        Returns: <bool>

        """
        try:
            query = "INSERT INTO users(username, password, email) VALUES({}, {}, {})"

            self.cursor.execute(query, (username, password, email))
            self.conn.commit()
            return True

        except Exception as e:
            return str(e)
