from .Base import Base
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import *
from sqlalchemy.sql import text
from sqlalchemy.sql.functions import current_timestamp

class SlackWorkspace(Base):
    __tablename__ = 'slack_workspaces'
    id = Column(String(255), primary_key=True, comment='Workspace ID')
    name = Column(String(255), nullable=False, comment='Workspace Name')
    domain = Column(String(255), nullable=False, comment='Workspace Domain')
    email_domain = Column(String(255), nullable=False, comment='Workspace Domain')
    icon = Column(Text, nullable=False, comment='Workspace Icons(JSON)')
    api_token = Column(Text, nullable=False, comment='API Token')
    created_at = Column(DateTime, nullable=False, server_default=current_timestamp())
    updated_at = Column(DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
