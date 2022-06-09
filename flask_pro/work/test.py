from flask_restful import Resource
from flask import request
from configs import app
import json


def say_hello():
    print("helllloooo ====")
    return


class Receive(Resource):
    b = []
    def __init__(self):
        self.num = 0
        print(self.num)
        self.a = []
        print(self.a)
        print(id(self.a))

    def get(self):
        # schedu.add_job(func=say_hello,trigger="interval", seconds=5,  id=str(id(say_hello)))
        app.scheduler.add_job(func=say_hello,trigger="interval", seconds=15,  id=str(id(say_hello)))
        return {"ok": 1}
    def post(self):
        data = request.get_json()

        print(request.cookies)

        self.num += 1
        print("num = ", self.num)
        self.a.append(self.num)
        print(self.a)
        self.b.append(self.num)
        print(id(self.b))
        print(self.b)

        param = {
            "status": "0",
            "id": "123"
        }
        return json.dumps(param)