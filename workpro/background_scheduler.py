from apscheduler.schedulers.background import BackgroundScheduler
import datetime
import time

scheduler = BackgroundScheduler()
def send_sms( name, task_id):
    print("你是 ", name, task_id)

def make_scheduler(name, task_id):

    scheduler.add_job(func=send_sms, args=(name, task_id,),
                      next_run_time=datetime.datetime.now() + datetime.timedelta(minutes=1), id=task_id)

def start_scheduler():
    scheduler.start()

start_scheduler()
while 1:
    time.sleep(10)
