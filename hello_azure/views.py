from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import JsonResponse
from .models import Video
import os
def index(request):
    print('Request for index page received')
    return render(request, 'index.html')


@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        video = Video(file=request.FILES['file'])
        video.save()
        return JsonResponse({'status': 'file uploaded'})
def obj_demo(request):
    return render(request, 'object_detection/demo.html')

def obj_result(request):
    return render(request, 'object_detection/result.html')

