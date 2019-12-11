import requests
import os

class SlackAPI:
    def __init__(self, access_token):
        self.access_token = access_token

    def get(self, path, qs={}):
        params = dict(**qs)
        params['token'] = self.access_token
        url = 'https://slack.com/api' + path
        return requests.get(url, params=params)

    def teamInfo(self, **kwargs):
        """
        ワークスペースの情報を取得
        """
        res = self.get('/team.info', kwargs)
        return res.status_code, res.json()

    def usersList(self, **kwargs):
        """
        メンバー情報を返却
        """
        res = self.get('/users.list', kwargs)
        return res.status_code, res.json()
    
    def channelsList(self, **kwargs):
        """
        チャンネル一覧を返却
        """
        res = self.get('/channels.list', kwargs)
        return res.status_code, res.json()
