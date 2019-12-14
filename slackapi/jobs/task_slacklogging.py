import click
from flask.cli import with_appcontext
from os import getenv
from flask import current_app as app
import datetime
from datetime import timedelta
from libs.models import *

@click.command('slacklogging', help='指定した日にちのSlackログを抽出')
@click.option('--target', required=True, help='日付指定(%Y%m%d)')
@with_appcontext
def task_slacklogging(target):
    dtstart = datetime.datetime.strptime(target, '%Y%m%d')
    dtend = dtstart + timedelta(days=1)
    workspaces = SlackWorkspace.query.all()
    for workspace in workspaces:
        print(workspace.api_token)