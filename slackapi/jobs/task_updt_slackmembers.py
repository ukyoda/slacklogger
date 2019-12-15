import click
from flask.cli import with_appcontext
from os import getenv
from flask import current_app as app
import datetime
from datetime import timedelta
from libs.models import *
from libs.slack import SlackAPI

@click.command('updt_slackmembers', help='指定したトークンのSlackユーザの情報を取得／更新')
@click.option('--workspace_id', required=True, help='SlackのWorkspace ID')
@with_appcontext
def task_updt_slackmembers(workspace_id, commit=True):
    run(workspace_id, commit=commit)

def run(workspace_id, commit=True):
    workspace = SlackWorkspace.query.filter(SlackWorkspace.id == workspace_id).one()
    token = workspace.api_token
    api = SlackAPI(token)
    code, res = api.usersList()
    if code != 200:
        logger.warn('API レスポンスエラー: code={}, response={}'.format(code, res))
        return 1
    for member in res['members']:
        # 1件取得
        slackMember = SlackMember.query \
            .filter(SlackMember.local_id==member['id'], SlackMember.team_id==workspace_id) \
            .first()
        if slackMember is None:
            slackMember = SlackMember()
            slackMember.setApiResponse(member, workspace.id)
            db.session.add(slackMember)
            app.logger.info(f'New Member: {slackMember.real_name}({slackMember.id})')
        else:
            slackMember.setApiResponse(member, workspace.id)
            app.logger.info(f'Update Member: {slackMember.real_name}({slackMember.id})')
    if commit:
        db.session.commit()        