import click
from flask.cli import with_appcontext
from os import getenv
from flask import current_app as app

@click.command('helloworld', help='Hello World.')
@with_appcontext
def task_helloworld():
    print('hello world!!!')
