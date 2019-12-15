import click
from flask.cli import with_appcontext
from os import getenv
from flask import current_app as app
import datetime
from datetime import timedelta
from libs.models import *
from libs.utils import datetime
from jobs.task_updt_slackmembers import run as run_updt_slackmembers
from jobs.task_updt_slackchannels import run as run_updt_slackchannels
from jobs.task_updt_slackdailylog import run as run_updt_slackdailylog

@click.command('slacklogging', help='指定した日にち')
@click.option('--from_date', required=False, help='メッセージ取得開始日(YYYYmmddで指定)/指定なしの場合は昨日の日付')
@click.option('--to_date', required=False, help='メッセージ取得完了日(YYYYmmddで指定)/指定なしの場合はfrom_date+1日')
@with_appcontext
def task_slacklogging(from_date=None, to_date=None):
    run(from_date, to_date)

def run(from_date=None, to_date=None):
    if from_date is None:
        from_date = datetime.yesterday_start() # 昨日の日付を指定
        from_date = from_date.strftime('%Y%m%d')
    workspaces = SlackWorkspace.query \
        .filter(SlackWorkspace.active_flag == True, SlackWorkspace.delete_flag == False) \
        .all()

    for workspace in workspaces:
        app.logger.info(f'Processing: {workspace.id}')
        app.logger.info('========== Update Slack Members ==========')
        run_updt_slackmembers(workspace.id, commit=False)
        app.logger.info('========== Update Slack Channels ==========')
        run_updt_slackchannels(workspace_id=workspace.id, commit=False)
        app.logger.info('========== Update Slack Messages ==========')
        channels = SlackChannel.query \
            .filter(SlackChannel.team_id==workspace.id) \
            .all()
        for channel in channels:
            run_updt_slackdailylog(channel.id, from_date, to_date, commit=False)
        db.session.commit()
        app.logger.info(f'---------- End({workspace.id}) ----------')