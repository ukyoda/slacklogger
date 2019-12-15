import click
from flask.cli import with_appcontext
from os import getenv
from flask import current_app as app
import datetime
from datetime import timedelta
from libs.models import *
from libs.slack import SlackAPI

@click.command('updt_slackchannels', help='指定したトークンのSlackチャンネルの情報を取得／更新')
@click.option('--workspace_id', required=True, help='SlackワークスペースID')
@with_appcontext
def task_updt_slackchannels(workspace_id, commit=True):
    slackWorkspace = SlackWorkspace.query.filter(SlackWorkspace.id==workspace_id).one()
    token = slackWorkspace.api_token
    api = SlackAPI(token)
    code, res = api.channelsList()
    if code != 200:
        logger.warn('API レスポンスエラー: code={}, response={}'.format(code, res))
        return 1
    for channel in res['channels']:
        # 1件取得
        slackChannel = SlackChannel.query \
            .filter(SlackChannel.id==f'{workspace_id}/{channel["id"]}') \
            .first()
        if slackChannel is None:
            slackChannel = SlackChannel()
            slackChannel.setApiResponse(channel, slackWorkspace.id)
            db.session.add(slackChannel)
            app.logger.info(f'New Channel: {slackChannel.name}({slackChannel.id}) ')
        else:
            slackChannel.setApiResponse(channel, slackWorkspace.id)
            app.logger.info(f'Update Channel: {slackChannel.name}({slackChannel.id}) ')
    if commit:
        db.session.commit()