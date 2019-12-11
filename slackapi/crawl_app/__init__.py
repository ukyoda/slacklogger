from libs.models import *
from libs.slack import SlackAPI
from libs.utils.datetime import today_start, yesterday_start, tomorrow_start, get_start_dt, from_timestamp
from datetime import timedelta

from crawl_app.crawl_members import crawl_members

import logging
logger = logging.getLogger(__name__)

def main():
    logging.basicConfig(level=logging.INFO)
    workspaces = session.query(SlackWorkspace).all()
    for workspace in workspaces:
        logger.info('[workspace={}] Backup Start!!'.format(workspace.name}))

        logger.info('[workspace={}] Update Member List'.format(workspace.name))
        crawl_members(workspace.token)

        logger.info('[workspace={}] Update Channel List'.format(workspace.name))
        crawl_channel(workspace.token, workspace.id)

        logger.info('[workspace={}] Backup End!!'.format(workspace.name))
    session.commit()

        
def crawl_channel(token, team_id):
    """
    チャンネルリスト更新
    """
    api = SlackAPI(token)
    code, res = api.channelsList()
    if code != 200:
        logger.warn('API レスポンスエラー: code={}, response={}'.format(code, res))
        return
    
    for channel in res['channels']:
        slackChannel = session \
            .query(SlackChannel) \
            .filter(SlackChannel.id==channel['id']) \
            .first()
        if slackChannel is None:
            slackChannel = SlackChannel()
            slackChannel.setApiResponse(channel, team_id)
            session.add(slackChannel)
        else:
            slackChannel.setApiResponse(channel, team_id)

def crawl_message(token, channel, target_dt=None):
    if target_dt is None:
        start_dt = yesterday_start()
        end_dt = today_start()
    else:
        start_dt = get_start_dt(target_dt)
        end_dt = start_dt + timedelta(days=1)
