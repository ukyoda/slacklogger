from flask import Flask
import flask
from config import BaseConfig

import logging
logging.basicConfig(level=logging.INFO)

# Setup Application (Flask App)
# ---------------------------------------
app = Flask(__name__)
app.config.from_object(BaseConfig)

# Setup Model (SQLAlchemy)
# ---------------------------------------
from libs.models import db
from flask_migrate import Migrate
db.init_app(app)
migrate = Migrate(app, db) 

# Setup Jobs (Click)
# ---------------------------------------
from jobs import job
app.cli.add_command(job)

# API Settings
# ---------------------------------------
from flask_restful import Api
from api import *
api = Api(app, prefix='/api/v1')
# api.add_resource(ApiWorkspace, '/workspace')
api.add_resource(ApiWorkspace, '/slack/ws', endpoint='workspaces')
api.add_resource(ApiWorkspace, '/slack/ws/<string:workspace_id>', endpoint='workspace')
api.add_resource(ApiChannel, '/slack/ch/<string:workspace_id>', endpoint='channels')
api.add_resource(ApiChannel, '/slack/ch/<string:workspace_id>/<string:local_id>', endpoint='channel')
api.add_resource(ApiMessage, '/slack/msg/<string:workspace_id>/<string:ch_local_id>', endpoint='messages')
api.add_resource(ApiMessage, '/slack/msg/<string:workspace_id>/<string:ch_local_id>/<string:ts>', endpoint='message')

if __name__ == '__main__':
    app.run()
