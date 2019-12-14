from flask import Flask
from jobs import job
from config import BaseConfig
from libs.models import db

app = Flask(__name__)
app.config.from_object(BaseConfig)

db.init_app(app)
app.cli.add_command(job)

if __name__ == '__main__':
    app.run()