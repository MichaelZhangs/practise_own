from __future__ import absolute_import, unicode_literals
from celery import Celery
from proj import celeryconfig

app = Celery("proj", broker=celeryconfig.broker_url, backend=celeryconfig.result_backend)
app.config_from_object("proj.celeryconfig")

app.autodiscover_tasks(["proj"])

