# cron設定
# ----------------------------------------------------------

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
import os
import subprocess
from config import SchedulerConfig as cfg

scheduler = BlockingScheduler()

# 定期実行 / 前日のSlackメッセージのバックアップをとる
@scheduler.scheduled_job(CronTrigger.from_crontab(cfg.job_slacklogging['crontab']))
def execute_job_slacklogging():
    """Slackのデイリーバックアップ"""
    subprocess.run(['flask', 'job', cfg.job_slacklogging['job']])

if __name__ == '__main__':
    scheduler.start()