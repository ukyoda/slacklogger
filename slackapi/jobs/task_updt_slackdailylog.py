import click
from flask.cli import with_appcontext
from os import getenv
from flask import current_app as app
from libs.utils.datetime import datetime, timedelta
from libs.models import *
from libs.slack import SlackAPI

@click.command('updt_slackdailylog', help='指定したトークンのSlackチャンネルの情報を取得／更新')
@click.option('--workspace_id', required=True, help='SlackワークスペースID')
@click.option('--channel_id', required=True, help='チャンネルID')
@click.option('--from_date', required=True, help='メッセージ取得開始日(YYYYmmddで指定)')
@click.option('--to_date', required=False, help='メッセージ取得完了日(YYYYmmddで指定)')
@with_appcontext
def task_updt_slackdailylog(workspace_id, channel_id, from_date, to_date, commit=True):
    slackChannel = SlackChannel.query.filter(
        SlackChannel.id==channel_id, SlackChannel.team_id==workspace_id).one()
    # APIトークン
    token = slackChannel.workspace.api_token
    # チャンネルID
    channel_id = slackChannel.id
    app.logger.info(f'{slackChannel.workspace.name}::{slackChannel.name}')
    api = SlackAPI(token)

    # 日付
    oldest = datetime.strptime(from_date, '%Y%m%d')
    latest = datetime.strptime(to_date, '%Y%m%d') if to_date is not None else oldest + timedelta(days=1)
    code, res = api.channelHistory(channel=channel_id,
                                   oldest=oldest.timestamp(), 
                                   latest=latest.timestamp(),
                                   count=1000)
    import json
    with open('tmp/check.json', 'w') as f:
        f.write(json.dumps(res, indent=2, ensure_ascii=False))
    # code, res = api.channelsList()
    # if code != 200:
    #     logger.warn('API レスポンスエラー: code={}, response={}'.format(code, res))
    #     return 1
    # for channel in res['channels']:
    #     # 1件取得
    #     slackChannel = SlackChannel.query \
    #         .filter(SlackChannel.id==channel['id']) \
    #         .first()
    #     if slackChannel is None:
    #         slackChannel = SlackChannel()
    #         slackChannel.setApiResponse(channel, slackWorkspace.id)
    #         db.session.add(slackChannel)
    #     else:
    #         slackChannel.setApiResponse(channel, slackWorkspace.id)
    # if commit:
    #     db.session.commit()        