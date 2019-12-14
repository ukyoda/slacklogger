import click
from flask.cli import with_appcontext
from os import getenv
from flask import current_app as app
import datetime
from datetime import timedelta
from libs.models import *
from libs.slack import SlackAPI

@click.command('updt_slackmembers', help='指定したトークン／日にちのSlackユーザの情報を取得／更新')
@click.option('--token', required=True, help='Slackアクセストークン')
@with_appcontext
def task_updt_slackmembers(token, commit=True):
    api = SlackAPI(token)
    code, res = api.usersList()
    if code != 200:
        logger.warn('API レスポンスエラー: code={}, response={}'.format(code, res))
        return 1
    for member in res['members']:
        # 1件取得
        slackMember = SlackMember.query \
            .filter(SlackMember.id==member['id']) \
            .first()
        if slackMember is None:
            slackMember = SlackMember()
            slackMember.setApiResponse(member)
            db.session.add(slackMember)
        else:
            slackMember.setApiResponse(member)
    if commit:
        db.session.commit()        