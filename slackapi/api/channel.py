from flask_restful import Resource
from libs.models import SlackChannel, SlackChannelSchema, NoResultFound
from flask import abort

class ApiChannel(Resource):
    
    def get(self, workspace_id, local_id=None):
        if local_id is None:
            return self._get_all(workspace_id)
        try:
            channel_id = f'{workspace_id}/{local_id}'
            channel = SlackChannel.query.filter(SlackChannel.id==channel_id).one()
            schema = SlackChannelSchema()
            return schema.dump(channel)
        except NoResultFound as e:
            abort(404)
        except:
            abort(500)

    def _get_all(self, workspace_id):
        channels = SlackChannel.query.filter(SlackChannel.team_id==workspace_id).all()
        schema = SlackChannelSchema(many=True)
        return schema.dump(channels)