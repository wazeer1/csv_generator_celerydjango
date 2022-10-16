from csv import writer
import csv
import json
from turtle import delay
from urllib import response
from django.shortcuts import HttpResponse, render
from .tasks import generate_csv, test_func
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def test(request):
    print('hai')
    test_func.delay()
    return HttpResponse("Done")


def index(request):
    return render(request,'web/index.html')

@csrf_exempt
def generate(request):
    file_name = request.POST["file_name"]
    number = request.POST["number"]
    generate_csv.apply_async(args=[number,file_name])
    # response = HttpResponse(content_type='text/csv')  
    # response['Content-Disposition'] = 'attachment; filename="file.csv"'  
    # writer = csv.writer(response)
    # writer.writerow(['1001', 'John', 'Domil', 'CA'])  
    # writer.writerow(['1002', 'Amit', 'Mukharji', 'LA', '"Testing"'])  
    # print(response)
    response_data={
        "hello":'response'
    }
    # return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    return HttpResponse((response), content_type='text/csv')