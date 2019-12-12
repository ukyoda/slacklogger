"""set_default_workspace

Revision ID: c3fb46e1dbd7
Revises: 4e8ca9710216
Create Date: 2019-12-12 00:09:31.944127

"""
from alembic import op
import sqlalchemy as sa
import os
from libs.models import SlackWorkspace, session
from libs.slack import SlackAPI

# revision identifiers, used by Alembic.
revision = 'c3fb46e1dbd7'
down_revision = '4e8ca9710216'
branch_labels = None
depends_on = None


def upgrade():
    token = os.getenv('DEFAULT_SLACK_TOKEN', '')
    if  os.getenv('APP_ENV') == 'product' or \
        token == '':
        print('No Token')
        return
    api = SlackAPI(token)
    code, res = api.teamInfo()
    slackWorkspace = SlackWorkspace()
    slackWorkspace.setApiResponse(res['team'], token)
    session.add(slackWorkspace)



def downgrade():
    op.execute('delete from slack_workspaces')
    
