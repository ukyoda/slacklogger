from flask_restful import Resource, reqparse
from libs.models import SlackMessage, SlackMessageSchema, NoResultFound
from flask import request
from flask import abort
from sqlalchemy import desc
from datetime import datetime

class ApiMessage(Resource):

    def get(self, workspace_id, ch_local_id, ts=None):
        if ts is None:
            return self._get_all(workspace_id, ch_local_id)
        try:
            message_id = f'{workspace_id}/{ch_local_id}/{ts}'
            message = SlackMessage.query.filter(SlackMessage.id==message_id).one()
            schema = SlackMessageSchema()
            return schema.dump(message)
        except NoResultFound as e:
            abort(404)
        except:
            abort(500)

    def _get_all(self, workspace_id, ch_local_id):
        parser = reqparse.RequestParser()
        parser.add_argument('count', type=int, default=100)
        parser.add_argument('from_ts', type=float)
        parser.add_argument('to_ts', type=float)
        args = parser.parse_args()
        channel_id = f'{workspace_id}/{ch_local_id}'
        query = SlackMessage.query.filter(SlackMessage.channel_id == channel_id)
        if args.from_ts is not None:
            from_dt = datetime.fromtimestamp(args.from_ts)
            query = query.filter(SlackMessage.post_time >= from_dt)
        if args.to_ts is not None:
            to_dt = datetime.fromtimestamp(args.to_ts)
            query = query.filter(SlackMessage.post_time < to_dt)
        query = query.order_by(desc(SlackMessage.post_time))
        query = query.limit(args.count)

        messages = query.all()
        schema = SlackMessageSchema(many=True)
        return schema.dump(messages)