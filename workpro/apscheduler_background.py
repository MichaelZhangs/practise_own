from apscheduler.schedulers.background import BackgroundScheduler
from flask import request
from flask import Flask, jsonify
from flask_restful import Api, Resource
import datetime
import  threading
from apscheduler.executors.pool import ThreadPoolExecutor
executors = {
    "default": ThreadPoolExecutor(3)
}
class Test(Resource):

    def __init__(self):
        self.scheduler = BackgroundScheduler(executors=executors)

    def send_sms(self, name, task_id):
        print("你是 ", name, task_id, threading.current_thread())

    def make_scheduler(self,name, task_id):

        self.scheduler.add_job(func=self.send_sms, args=(name, task_id,),
                          next_run_time=datetime.datetime.now() + datetime.timedelta(minutes=1), id=task_id)

    def start_sched(self, name, task_id):
        self.make_scheduler(name, task_id)
        self.scheduler.start()

    def get(self):
        data = request.args
        name = data.get("name", "")
        task_id = data.get("task_id", "")
        self.start_sched(name, task_id)
        return jsonify(200, {"status": "ok"})
app = Flask(__name__)
api = Api(app)
api.add_resource(Test, "/test_get")
if __name__ == '__main__':
    app.run("127.0.0.1", port=8888)