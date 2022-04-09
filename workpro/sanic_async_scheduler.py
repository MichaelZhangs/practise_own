from sanic import Sanic
from sanic.views import HTTPMethodView
from apscheduler.schedulers.background import BackgroundScheduler
from sanic.response import  json
import  threading
from apscheduler.executors.pool import ThreadPoolExecutor
import datetime
import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler

executors = {
    "default": ThreadPoolExecutor(3)
}


class SanicView(HTTPMethodView):
    def __init__(self):
        # self.scheduler = BackgroundScheduler(executors=executors)
        self.scheduler = AsyncIOScheduler(executors=executors)
    def send_sms(self, name, task_id):
        print("你是 ", name, task_id, threading.current_thread())

    # def run(self, name, task_id):
    #     loop = asyncio.new_event_loop()
    #     tasks = [
    #         loop.create_task(self.send_sms(name, task_id))
    #     ]
    #     loop.run_until_complete(asyncio.wait(tasks))

    def make_scheduler(self,name, task_id):

        self.scheduler.add_job(func=self.send_sms, args=(name, task_id,),
                          next_run_time=datetime.datetime.now() + datetime.timedelta(seconds=3), id=task_id)

    def start_sched(self, name, task_id):
        self.make_scheduler(name, task_id)
        print(self.scheduler.get_jobs())
        self.scheduler.start()

    async def get(self, request):
        data = request.args
        name = data.get("name", "")
        headers = request.headers
        # print(headers)
        print(headers.get("user_id", ""))
        # print(request.cookies)

        task_id = data.get("task_id", "")
        self.start_sched(name, task_id)
        return json({"code":200, "msg": "success"})

    async def post(self, request):
        data = request.json
        name = data.get("name", "")
        task_id = data.get("task_id", "")
        print(name, task_id)
        return json({"code": 200, "msg": "post success"})


app = Sanic(__name__)
app.add_route(SanicView.as_view(), "/sanic_test")
if __name__ == '__main__':
    app.run("127.0.0.1", port=8000)