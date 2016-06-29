import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


def get_connection_string():
    user = os.environ['MYSQL_USER']
    password = os.environ['MYSQL_PASSWORD']
    host = os.environ['MYSQL_HOST_ADDRESS']
    port = os.environ['MYSQL_PORT']
    database = os.environ['MYSQL_DATABASE']
    return 'mysql://{0}:{1}@{2}:{3}/{4}'.format(user, password, host, port, database)
