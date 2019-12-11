from .Base import Base
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import *
from sqlalchemy.sql import text
from sqlalchemy.sql.functions import current_timestamp

class SlackMember(Base):
    __tablename__ = 'slack_members'
    id = Column(String(64), primary_key=True, comment='User ID(Workspace)')
    team_id = Column(String(64), ForeignKey('slack_workspaces.id'), nullable=False, comment='Team ID')
    name = Column(String(128), nullable=False, comment='User Name')
    deleted = Column(Boolean, nullable=False, comment='Delete Flag')
    color = Column(String(64), nullable=False, comment='Color')
    real_name = Column(String(128), nullable=False, comment='Real Name')
    tz = Column(String(64), nullable=True, comment='Timezone')
    tz_offset = Column(Integer, nullable=False, comment='Timezone Offset')
    image_24 = Column(Text, nullable=False, comment='Avatar Icon(24)')
    image_32 = Column(Text, nullable=False, comment='Avatar Icon(32)')
    image_48 = Column(Text, nullable=False, comment='Avatar Icon(48)')
    image_72 = Column(Text, nullable=False, comment='Avatar Icon(72)')
    image_192 = Column(Text, nullable=False, comment='Avatar Icon(192)')
    image_512 = Column(Text, nullable=False, comment='Avatar Icon(2512')
    is_bot = Column(Boolean, nullable=False, comment='Bot Flag')
    is_owner = Column(Boolean, nullable=False, comment='Owner Flag')
    is_admin = Column(Boolean, nullable=False, comment='Admin Flag')
    created_at = Column(DateTime, nullable=False, server_default=current_timestamp())
    updated_at = Column(DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))

    def setApiResponse(self, member):
        """
        Slack APIのレスポンス結果をモデルにセット
        
        Arguments:
            * member
                * Slackのusers.listのmembersリストの1要素
        """
        self.id=member['id']
        self.team_id=member['team_id']
        self.name=member['name']
        self.deleted=member['deleted']
        self.color=member['color']
        self.real_name=member['real_name']
        self.tz=member['tz']
        self.tz_offset=member['tz_offset']
        self.image_24=member['profile']['image_24']
        self.image_32=member['profile']['image_32']
        self.image_48=member['profile']['image_48']
        self.image_72=member['profile']['image_72']
        self.image_192=member['profile']['image_192']
        self.image_512=member['profile']['image_512']
        self.is_bot=member['is_bot']
        self.is_owner=member['is_owner']
        self.is_admin=member['is_admin']