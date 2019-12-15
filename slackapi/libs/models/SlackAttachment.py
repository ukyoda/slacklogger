from .Base import db
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import *
from sqlalchemy.sql import text as _text
from sqlalchemy.sql.functions import current_timestamp

class SlackAttachment(db.Model):
    """
    Slack添付(リンク？)情報
    """
    __tablename__ = 'slack_attachments'
    id = Column(String(128), primary_key=True, comment='Primary Key({message_id}/{attachment_id})')
    message_id = Column(String(128), ForeignKey('slack_messages.id'), comment='Message ID')
    attachment_id = Column(String(64), index=True, comment='Attachment id')
    service_name = Column(String(64), comment='サービスの名前(サイト名と思う)')
    title = Column(String(128), comment='ページタイトルと思う')
    text = Column(Text, comment='ページの概要')
    original_url = Column(Text, nullable=True, comment='URL情報')
    thumb_url = Column(Text, comment='サムネイル画像')
    service_icon = Column(Text, comment='サイトのアイコンが像')
    created_at = Column(DateTime, nullable=False, server_default=current_timestamp())
    updated_at = Column(DateTime, nullable=False, server_default=_text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))

    def setApiResponse(self, attachment, message_id):
        self.id = f'{message_id}/{attachment["id"]}'
        self.message_id = message_id
        self.attachment_id = attachment['id']
        self.service_name = attachment['service_name']
        self.title = attachment['title']
        self.text = attachment['text']
        self.original_url = attachment['original_url']
        self.thubm_url = attachment['thumb_url'] if 'thumb_url' in attachment else None
        self.service_icon = attachment['service_icon']
    