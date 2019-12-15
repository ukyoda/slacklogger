from flask_restful import Resource
from libs.models import SlackWorkspace, SlackWorkspaceSchema, NoResultFound

from flask import abort
class ApiWorkspace(Resource):
    
    def get(self, workspace_id=None):
        if workspace_id is None:
            return self._get_all()
        try:
            workspace = SlackWorkspace.query.filter(SlackWorkspace.id==workspace_id).one()
            schema = SlackWorkspaceSchema()
            return schema.dump(workspace)
        except NoResultFound as e:
            abort(404)
        except:
            abort(500)

    def _get_all(self):
        workspaces = SlackWorkspace.query.all()
        schema = SlackWorkspaceSchema(many=True)
        return schema.dump(workspaces)