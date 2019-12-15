from .Base import db
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import *
from sqlalchemy.sql import text
from sqlalchemy.sql.functions import current_timestamp

class SlackWorkspace(db.Model):
    __tablename__ = 'slack_workspaces'
    id = Column(String(64), primary_key=True, comment='Workspace ID')
    name = Column(String(128), nullable=False, comment='Workspace Name')
    domain = Column(String(64), nullable=False, comment='Workspace Domain')
    email_domain = Column(String(64), nullable=True, comment='Workspace Domain')
    image_34 = Column(Text, nullable=False, comment='Avatar Icon(34)')
    image_44 = Column(Text, nullable=False, comment='Avatar Icon(44)')
    image_68 = Column(Text, nullable=False, comment='Avatar Icon(68)')
    image_88 = Column(Text, nullable=False, comment='Avatar Icon(88)')
    image_102 = Column(Text, nullable=False, comment='Avatar Icon(102)')
    image_132 = Column(Text, nullable=False, comment='Avatar Icon(132)')
    api_token = Column(Text, nullable=False, comment='API Token')
    active_flag = Column(Text, nullable=False, default=True, comment='Crawler Active Flag')
    delete_flag = Column(Boolean, nullable=False, default=False, comment='Delete flag')
    created_at = Column(DateTime, nullable=False, server_default=current_timestamp())
    updated_at = Column(DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    # members = relationship('SlackMember', order_by='asc(SlackMember.real_name)', lazy='dynamic')
    # channels = relationship('SlackChannel', order_by='asc(SlackChannel.created)', lazy='dynamic')

    def setApiResponse(self, workspace, api_token):
        self.id = workspace['id']
        self.name = workspace['name']
        self.domain = workspace['email_domain']
        self.image_34=workspace['icon']['image_34']
        self.image_44=workspace['icon']['image_44']
        self.image_68=workspace['icon']['image_68']
        self.image_88=workspace['icon']['image_88']
        self.image_102=workspace['icon']['image_102']
        self.image_132=workspace['icon']['image_132']
        self.api_token = api_token
    