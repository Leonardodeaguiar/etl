import mysql.connector as mysql


class DatabaseConnector:
    connection = None

    @classmethod
    def connect(cls):
        db_connection = mysql.connect(
            host="localhost",
            port=3306,
            database="pipeline_db",
            user="root",
            passwd="l30nardo",
        )
        cls.connection = db_connection
