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
db.init_app(app)

# Setup Jobs (Click)
# ---------------------------------------
from jobs import job
app.cli.add_command(job)

if __name__ == '__main__':
    app.run()
