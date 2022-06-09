# encoding:utf8

from configs import app
from flask_apscheduler import APScheduler
from routers import test_bp


app.register_blueprint(test_bp, url_prefix='/v1')

if __name__ == '__main__':
    schedu = APScheduler()
    schedu.init_app(app)
    schedu.start()
    app.scheduler = schedu
    app.run(host="127.0.0.1", port=8888, debug=True)
