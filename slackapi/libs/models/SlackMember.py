from .Base import Base
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import *
from sqlalchemy.sql import text
from sqlalchemy.sql.functions import current_timestamp

class SlackMember(Base):
    __tablename__ = 'slack_members'
    id = Column(String(64), primary_key=True, comment='User ID(Workspace)')
    team_id = Column(String(64), nullable=False, index=True, comment='Team ID')
    name = Column(String(128), nullable=False, comment='User Name')
    deleted = Column(Boolean, nullable=False, comment='Delete Flag')
    color = Column(String(64), nullable=False, comment='Color')
    real_name = Column(String(128), nullable=False, comment='Real Name')
    tz = Column(String(64), nullable=False, comment='Timezone')
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
