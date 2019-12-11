from .Base import Base
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer
from sqlalchemy.sql.sqltypes import Text
from sqlalchemy.sql.sqltypes import String

class SlackWorkspace(Base):
    __tablename__ = 'slack_workspaces'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    api_token = Column(Text, nullable=False)