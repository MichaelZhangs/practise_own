from flask import Blueprint
from flask_restful import Api
from work.test import Receive


test_bp = Blueprint("routers", __name__)

api = Api(test_bp)
api.add_resource(Receive, "/send_post")