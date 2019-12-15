"""change_colname

Revision ID: c049d36c5f5d
Revises: 18083b656fc0
Create Date: 2019-12-15 18:46:03.303146

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c049d36c5f5d'
down_revision = '18083b656fc0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('slack_members', sa.Column('local_id', sa.String(length=64), nullable=True, comment='Slack UserID'))
    op.create_index(op.f('ix_slack_members_local_id'), 'slack_members', ['local_id'], unique=False)
    op.drop_index('ix_slack_members_user_id', table_name='slack_members')
    op.drop_column('slack_members', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('slack_members', sa.Column('user_id', mysql.VARCHAR(collation='utf8mb4_general_ci', length=64), nullable=True, comment='Slack UserID'))
    op.create_index('ix_slack_members_user_id', 'slack_members', ['user_id'], unique=False)
    op.drop_index(op.f('ix_slack_members_local_id'), table_name='slack_members')
    op.drop_column('slack_members', 'local_id')
    # ### end Alembic commands ###
