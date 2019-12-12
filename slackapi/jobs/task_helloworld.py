import click
from flask.cli import with_appcontext

@click.command('helloworld', help='Hello World.')
@with_appcontext
def task_helloworld():
    print('hello world!!!')