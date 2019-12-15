from flask.cli import AppGroup
from jobs.task_helloworld import task_helloworld
from jobs.task_regist_slack import task_regist_slack
from jobs.task_slacklogging import task_slacklogging
from jobs.task_updt_slackmembers import task_updt_slackmembers
from jobs.task_updt_slackchannels import task_updt_slackchannels
from jobs.task_updt_slackdailylog import task_updt_slackdailylog
from jobs.task_slacklogging import task_slacklogging

# jobグループを作成
job = AppGroup('job')

# task関連のコマンドを追加していく
job.add_command(task_helloworld)
job.add_command(task_regist_slack)
job.add_command(task_slacklogging)
job.add_command(task_updt_slackmembers)
job.add_command(task_updt_slackchannels)
job.add_command(task_updt_slackdailylog)
job.add_command(task_slacklogging)