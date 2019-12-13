import os
from os import getenv

class BaseConfig:
    # Database Settings
    db_url = "{}+{}://{}:{}@{}:{}/{}".format(
        'mysql', 'pymysql',
        getenv('MYSQL_USER'), getenv('MYSQL_PASSWORD'),
        getenv('MYSQL_HOST'), getenv('MYSQL_PORT'),
        getenv('MYSQL_DATABASE')
    )

