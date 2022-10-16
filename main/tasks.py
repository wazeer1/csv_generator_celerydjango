import csv
import os
import random
import string

from django.http import HttpResponse
from celery import shared_task
from main.models import CsvFiles
# from main.views import generate



@shared_task(bind=True)
def generate_csv(self,*args, **kwargs):
    number = args[0]
    file_name = args[1]
    
    with open(f'media/{file_name}.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',',quoting=csv.QUOTE_MINIMAL)
        for i in range(int(number)):
            res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
            num = random.randint(9000,10000)
            csv_writer.writerow([res, num])
    file = os.path.join('/media',f'{file_name}.csv')
    generated = CsvFiles.objects.create(
        name = file_name,
        file = file,
    )
    return "response"




