"""CreateSlackWorkspace

Revision ID: 0e694bc8aa36
Revises: 
Create Date: 2019-12-11 12:09:23.609581

"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))
from alembic import op
import sqlalchemy as sa
from libs.slack import SlackAPI
import json

# revision identifiers, used by Alembic.
revision = '0e694bc8aa36'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    table = op.create_table('slack_workspaces',
        sa.Column('id', sa.String(length=64), nullable=False, comment='Workspace ID'),
        sa.Column('name', sa.String(length=128), nullable=False, comment='Workspace Name'),
        sa.Column('domain', sa.String(length=64), nullable=False, comment='Workspace Domain'),
        sa.Column('email_domain', sa.String(length=64), nullable=False, comment='Workspace Domain'),
        sa.Column('icon', sa.Text(), nullable=False, comment='Workspace Icons(JSON)'),
        sa.Column('api_token', sa.Text(), nullable=False, comment='API Token'),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=False),
        sa.PrimaryKeyConstraint('id')
        )
    # ### end Alembic commands ###
    try:
        slack_token = os.getenv('SLACK_TOKEN', '')
        if slack_token == '':
            return
        api = SlackAPI(slack_token)
        rescode, teamInfo = api.teamInfo()
        if rescode == 200:
            teamInfo = teamInfo['team']
            teamInfo['icon'] = json.dumps(teamInfo['icon'])
            teamInfo['api_token'] = slack_token
        op.bulk_insert(table, [teamInfo])
    except:
        import traceback
        traceback.print_exc()
        downgrade()
        op.drop_table('slack_workspaces')
        raise RuntimeError('Migration Error')    

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('slack_workspaces')
    # ### end Alembic commands ###
