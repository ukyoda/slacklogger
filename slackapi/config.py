import os
from os import getenv

class BaseConfig:
    # Database Settings
    # ------------------------------------------------------
    SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=UTF8MB4".format(
        'mysql', 'pymysql',
        getenv('MYSQL_USER'), getenv('MYSQL_PASSWORD'),
        getenv('MYSQL_HOST'), getenv('MYSQL_PORT'),
        getenv('MYSQL_DATABASE')
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

