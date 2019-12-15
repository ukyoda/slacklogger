#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy import *
from sqlalchemy.orm import *
from os import getenv
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

Base = db.Model