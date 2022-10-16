from __future__ import absolute_import,unicode_literals
import os
from time import timezone

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'csv_generate.settings')

app = Celery('csv_generate')
app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Kolkata')

app.config_from_object(settings, namespace='CELERY')

#celery beat settings


app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request:{self.request!r}')

