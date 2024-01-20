from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .forms import VideoForm
from .models import Video
import os

def index(request):
    print('Request for index page received')
    return render(request, 'index.html')


def upload_file(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            try:
                video = Video.objects.get(title=title)
                video.video = form.cleaned_data['video']
                video.save()
            except Video.DoesNotExist:
                form.save()
            return JsonResponse({'status': 'file uploaded'})
        else:
            # フォームが無効な場合はエラーを返します
            return JsonResponse({'status': 'invalid form'}, status=400)
    else:
        form = VideoForm()
        # GET リクエストの場合はフォームを含む HTML ページを返します
        return render(request, 'object_detection/demo.html', {'form': form})


def obj_demo(request):
    return render(request, 'object_detection/demo.html')

def obj_result(request):
    return render(request, 'object_detection/result.html')

