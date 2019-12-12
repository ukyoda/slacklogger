from .Base import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import *
from sqlalchemy.sql import text
from sqlalchemy.sql.functions import current_timestamp
from ..utils.datetime import from_timestamp

class SlackChannel(Base):
    __tablename__ = 'slack_channels'
    id = Column(String(64), primary_key=True, comment='Channel ID')
    team_id = Column(String(64), ForeignKey('slack_workspaces.id'), comment='Workspace ID')
    name = Column(String(128), nullable=False, comment='Channel Name')
    created = Column(DateTime, nullable=False, comment='Channel Create Datetime')
    topic = Column(Text, comment='Channel Topic')
    purpose = Column(Text, comment='Channel Purpose')
    created_at = Column(DateTime, nullable=False, server_default=current_timestamp())
    updated_at = Column(DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    
    def setApiResponse(self, channel, team_id):
        self.id = channel['id']
        self.team_id = team_id
        self.name = channel['name']
        self.created = from_timestamp(channel['created'])
        self.topic = channel['topic']['value']
        self.purpose = channel['purpose']['value']