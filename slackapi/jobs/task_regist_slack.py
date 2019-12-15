import click
from flask.cli import with_appcontext
from os import getenv
from flask import current_app as app
from libs.slack import SlackAPI
from libs.models import db, SlackWorkspace

@click.command('regist_slack', help='Register Slack Workspace')
@click.option('--token', default=getenv('DEFAULT_SLACK_TOKEN', ''), help='登録するSlackAPIトークン')
@with_appcontext
def task_regist_slack(token):
    """デフォルトSlackTokeに従い、ワークスペースを登録"""
    run(token)

def run(token):
    # データ更新
    api = SlackAPI(token)
    code, res = api.teamInfo()

    if code != 200:
        app.logger.error('APIでエラーが発生しました')
        app.logger.error(res)
        return 1
    ws = SlackWorkspace.query.filter(SlackWorkspace.id == res['team']['id']).first()
    # データがあれば何もしない
    if ws is None:
        app.logger.info('Insert')
        ws = SlackWorkspace()
        ws.setApiResponse(res['team'], token)
        db.session.add(ws)
    else:
        app.logger.info('Update')
        ws.setApiResponse(res['team'], token)
    db.session.commit()
    app.logger.info(f'Complete(WorkspaceID= {ws.id} ) !!')
