import click
from flask.cli import with_appcontext
from os import getenv
from flask import current_app as app
from libs.utils.datetime import datetime, timedelta
from libs.models import *
from libs.slack import SlackAPI

@click.command('updt_slackdailylog', help='指定したトークンのSlackチャンネルの情報を取得／更新')
@click.option('--channel_id', required=True, help='チャンネルID(team_id/local_id)')
@click.option('--from_date', required=True, help='メッセージ取得開始日(YYYYmmddで指定)')
@click.option('--to_date', required=False, help='メッセージ取得完了日(YYYYmmddで指定)')
@with_appcontext
def task_updt_slackdailylog(channel_id, from_date, to_date=None, commit=True):
    run(channel_id, from_date, to_date=to_date, commit=commit)

def run(channel_id, from_date, to_date=None, commit=True):
    # 必要な情報をDBから取得
    slackChannel = SlackChannel.query.filter(SlackChannel.id==channel_id).one()
    token = slackChannel.workspace.api_token
    app.logger.info(f'{slackChannel.workspace.name}::{slackChannel.name}')

    # 日付
    oldest = datetime.strptime(from_date, '%Y%m%d')
    latest = datetime.strptime(to_date, '%Y%m%d') if to_date is not None else oldest + timedelta(days=1)

    # APIコール
    api = SlackAPI(token)
    code, res = api.channelHistory(channel=slackChannel.local_id,
                                   oldest=oldest.timestamp(), 
                                   latest=latest.timestamp(),
                                   count=1000)
    for message in res['messages']:
        slackMessage = SlackMessage.query.filter(
            SlackMessage.channel_id == slackChannel.id, SlackMessage.ts == message['ts']).first()
        if slackMessage is None:
            slackMessage = SlackMessage()
            slackMessage.setApiResponse(message, slackChannel.team_id, slackChannel.id)
            db.session.add(slackMessage)
        else:
            slackMessage.setApiResponse(message, slackChannel.team_id, slackChannel.id)
        if 'attachments' in message:
            _setattachment(slackMessage.id, message['attachments'])
        if 'files' in message:
            _setfiles(slackMessage.id, message['files'])

    if commit:
        db.session.commit()

def _setattachment(message_id, attachments):
    for attachment in attachments:
        slackAttachment = SlackAttachment.query \
            .filter(SlackAttachment.message_id == message_id) \
            .filter(SlackAttachment.attachment_id == attachment['id']) \
            .first()
        if slackAttachment is None:
            slackAttachment = SlackAttachment()
            slackAttachment.setApiResponse(attachment, message_id)
            db.session.add(slackAttachment)
        else:
            slackAttachment.setApiResponse(attachment, message_id)

def _setfiles(message_id, files):
    for file in files:
        slackFile = SlackFile.query \
            .filter(SlackFile.message_id == message_id) \
            .filter(SlackFile.file_id == file['id']) \
            .first()
        if slackFile is None:
            slackFile = SlackFile()
            slackFile.setApiResponse(file, message_id)
            db.session.add(slackFile)
        else:
            slackFile.setApiResponse(file, message_id)