from .SlackWorkspace import SlackWorkspace
from .SlackMember import SlackMember
from .SlackChannel import SlackChannel
from .SlackMessage import SlackMessage
from .SlackFile import SlackFile
from .SlackAttachment import SlackAttachment
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

class SlackWorkspaceSchema(ModelSchema):
    class Meta:
        model = SlackWorkspace

class SlackChannelSchema(ModelSchema):
    class Meta:
        model = SlackChannel
    workspace = fields.Nested(SlackWorkspaceSchema)

class SlackMemberSchema(ModelSchema):
    class Meta:
        model = SlackMember
    workspace = fields.Nested(SlackWorkspaceSchema)

class SlackAttachmentSchema(ModelSchema):
    class Meta:
        model = SlackAttachment

class SlackFileSchema(ModelSchema):
    class Meta:
        model = SlackFile

class SlackMessageSchema(ModelSchema):
    class Meta:
        model = SlackMessage
    files = fields.Nested(SlackFileSchema, many=True)
    attachments = fields.Nested(SlackAttachmentSchema, many=True)
    author = fields.Nested(SlackMemberSchema)
    channel = fields.Nested(SlackChannelSchema)

