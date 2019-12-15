from .Base import db
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import *
from sqlalchemy.sql import text as _text
from sqlalchemy.sql.functions import current_timestamp

class SlackFile(db.Model):
    """
    Slackファイル情報
    """
    __tablename__ = 'slack_files'
    id = Column(String(128), primary_key=True, comment='Primary Key({message_id}/{file_id})')
    message_id = Column(String(128), ForeignKey('slack_messages.id'), comment='Message ID')
    file_id = Column(String(64), primary_key=True, comment='File_ID')
    title = Column(String(128), comment='ファイル名')
    filetype = Column(String(64), index=True, comment='ファイル種別')
    size = Column(Integer, comment='ファイルサイズ(Byte??)')
    permalink = Column(Text, nullable=True, comment='ファイルリンク(パーマリンク)')
    created_at = Column(DateTime, nullable=False, server_default=current_timestamp())
    updated_at = Column(DateTime, nullable=False, server_default=_text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))

    def setApiResponse(self, file, message_id):
        self.id = f'{message_id}/{file["id"]}'
        self.message_id = message_id
        self.file_id = file['id']
        self.title = file['title']
        self.filetype = file['filetype']
        self.size = file['size']
        self.permalink = file['permalink']