from .Base import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import *
from sqlalchemy.sql import text
from sqlalchemy.sql.functions import current_timestamp

class SlackMessage(Base):
    __tablename__ = 'slack_messages'
    id = Column(String(64), primary_key=True, comment='Message ID')
    channel_id = Column(String(64), ForeignKey('slack_channels.id'), comment='Channel ID')
    author_id = Column(String(64), ForeignKey('slack_members.id'), comment='User ID(Workspace)')
    text = Column(Text, nullable=False, comment='Text Body')
    created = Column(DateTime, nullable=False, comment='Channel Create Datetime')
    created_at = Column(DateTime, nullable=False, server_default=current_timestamp())
    updated_at = Column(DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    