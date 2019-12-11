#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy import *
from sqlalchemy.orm import *
from os import getenv

dialect = "mysql"
driver = "pymysql"
username = getenv('MYSQL_USER')
password = getenv('MYSQL_PASSWORD')
host = getenv('MYSQL_HOST')
port = getenv('MYSQL_PORT')
database = getenv('MYSQL_DATABASE')
db_url = "{}+{}://{}:{}@{}:{}/{}".format(
    dialect,
    driver,
    username,
    password,
    host,
    port,
    database
)

ENGINE = create_engine(db_url, echo=False)
session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)
)

Base = declarative_base()