from .Base import db
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import *
from sqlalchemy.sql import text as _text
from sqlalchemy.sql.functions import current_timestamp
from .SlackAttachment import SlackAttachment

class SlackMessage(db.Model):
    """
    Slackメッセージ情報
    """
    __tablename__ = 'slack_messages'
    id = Column(String(128), primary_key=True, comment='Message ID({workspace_id}/{channel_id}/{ts})')
    channel_id = Column(String(64), ForeignKey('slack_channels.channel_id'), comment='Channel ID')
    user_id = Column(String(64), ForeignKey('slack_members.user_id'), comment='User ID(Workspace)')
    text = Column(Text, nullable=False, comment='Text Body')
    ts = Column(String(64), nullable=False, index=True, comment='Post Timestamp')
    thread_ts = Column(String(64), comment='Thread Timestamp')
    created_at = Column(DateTime, nullable=False, server_default=current_timestamp())
    updated_at = Column(DateTime, nullable=False, server_default=_text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    files = relationship('SlackFile', order_by='asc(SlackFile.filetype)', lazy='dynamic')
    attachments = relationship('SlackAttachment', order_by='asc(SlackAttachment.id)', lazy='dynamic')

    def setApiResponse(self, message, team_id, channel_id):
        self.id = f'{team_id}/{channel_id}/{message["ts"]}'
        self.channel_id = channel_id
        self.user_id = message['user']
        self.text = message['text']
        self.ts = message['ts']
        if 'thread_ts' in message:
            self.thread_ts = float(message['thread_ts'])
