import json
from django.shortcuts import HttpResponse, render
from .tasks import generate_csv
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request,'web/index.html')

@csrf_exempt
def generate(request):
    file_name = request.POST["file_name"]
    number = request.POST["number"]
    generate_csv.apply_async(args=[number,file_name])
    response_data={
        "hello":'response'
    }
    return HttpResponse(json.dumps(response_data), content_type='application/javascript')