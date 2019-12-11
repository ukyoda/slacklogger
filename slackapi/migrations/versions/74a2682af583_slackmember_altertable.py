"""slackmember_altertable

Revision ID: 74a2682af583
Revises: e63dd1ac734d
Create Date: 2019-12-11 16:32:27.501740

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '74a2682af583'
down_revision = 'e63dd1ac734d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('slack_members', 'tz',
               existing_type=mysql.VARCHAR(collation='utf8mb4_general_ci', length=64),
               nullable=True,
               existing_comment='Timezone')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('slack_members', 'tz',
               existing_type=mysql.VARCHAR(collation='utf8mb4_general_ci', length=64),
               nullable=False,
               existing_comment='Timezone')
    # ### end Alembic commands ###
