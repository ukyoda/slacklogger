from flask.cli import AppGroup
from jobs.task_helloworld import task_helloworld

# jobグループを作成
job = AppGroup('job')

# task関連のコマンドを追加していく
job.add_command(task_helloworld)