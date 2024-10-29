from sched import scheduler
from apscheduler.schedulers.blocking import BlockingScheduler

import stack_overflow_page

scheduler = BlockingScheduler()

@scheduler.scheduled_job("interval", hours=1)
def access_stack_overflow_page():
    stack_overflow_page.login()

scheduler.start()