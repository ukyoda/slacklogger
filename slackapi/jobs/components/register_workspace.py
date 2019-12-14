from libs.models import SlackWorkspace
from libs.slack import SlackAPI

def register_workspace(slack_token):
    api = SlackAPI(slack_token)
    code, res = api.teamInfo()
    print(code)
    print(res)