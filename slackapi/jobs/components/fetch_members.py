from libs.slack import SlackAPI
from libs.models import *
import logging 
logger = logging.getLogger(__name__)

def crawl_members(token):
    """
    メンバーリスト更新
    """
    api = SlackAPI(token)
    code, res = api.usersList()
    if code != 200:
        logger.warn('API レスポンスエラー: code={}, response={}'.format(code, res))
        return

    for member in res['members']:
        # 1件取得
        slackMember = session \
            .query(SlackMember) \
            .filter(SlackMember.id==member['id']) \
            .first()
        if slackMember is None:
            slackMember = SlackMember()
            slackMember.setApiResponse(member)
            db.session.add(slackMember)
        else:
            slackMember.setApiResponse(member)
