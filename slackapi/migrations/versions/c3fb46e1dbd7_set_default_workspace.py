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
    if code != 200:
        raise RuntimeError('Migration Error(Seeder)')
    slackWorkspace = SlackWorkspace()
    slackWorkspace.setApiResponse(res['team'], token)
    session.add(slackWorkspace)
    team = res['team']
    record = dict(
        id = team['id'],
        name = team['name'],
        domain = team['email_domain'],
        image_34=team['icon']['image_34'],
        image_44=team['icon']['image_44'],
        image_68=team['icon']['image_68'],
        image_88=team['icon']['image_88'],
        image_102=team['icon']['image_102'],
        image_132=team['icon']['image_132'],
        api_token = token
    )
    table = sa.sql.table('slack_workspaces', 
        sa.column('id'))
    op.bulk_insert('slack_workspaces', [record])



def downgrade():
    op.execute('delete from slack_workspaces')
    
