from django.shortcuts import render
from django.views.generic import View
from .forms import FileUploadSampleForm
from django.http import JsonResponse
from django.urls import reverse
from .application import object_detection_django ,segmentation_django
import os
def index(request):
    return render(request, 'index.html')

class IndexView(View):
    def get(self, request, *args, **kwargs):
        form = FileUploadSampleForm()
        return render(request, 'object_detection/demo.html', {"form": form})

    def post(self, request, *args, **kwargs):
        """POSTリクエスト用のメソッド"""
        form = FileUploadSampleForm(request.POST, request.FILES)

        if not form.is_valid():
            return render(request, 'object_detection/demo.html', {"form": form})

        filename_save = form.save()
        
        context = {
            'form': form,
            'filename_save': filename_save,
        }
        
        output_video_path = os.path.join('media', 'upload', 'output.mp4')
        input_video_path = os.path.join('media', 'upload', 'input.mp4')
        object_detection_django.run_object_detection(input_video_path,output_video_path)
        #zzz = ai.run()
        redirect_url = reverse('obj_result')
        # 処理が完了したら、リダイレクト先のURLを含むJSONを返す
        return JsonResponse({'redirectUrl': redirect_url})
    
class seg_demo(View):
    def get(self, request, *args, **kwargs):
        form = FileUploadSampleForm()
        return render(request, 'segmentation/demo.html', {"form": form})

    def post(self, request, *args, **kwargs):
        """POSTリクエスト用のメソッド"""
        form = FileUploadSampleForm(request.POST, request.FILES)

        if not form.is_valid():
            return render(request, 'segmentation/demo.html', {"form": form})

        filename_save = form.save()
        
        context = {
            'form': form,
            'filename_save': filename_save,
        }
        
        output_video_path = os.path.join('media', 'upload', 'output.mp4')
        input_video_path = os.path.join('media', 'upload', 'input.mp4')
        segmentation_django.run_segmentation(input_video_path,output_video_path)
        #zzz = ai.run()
        redirect_url = reverse('seg_result')
        # 処理が完了したら、リダイレクト先のURLを含むJSONを返す
        return JsonResponse({'redirectUrl': redirect_url})



# IndexViewクラスのインスタンスを作成し、関数ビューとして使用可能にする
obj_demo = IndexView.as_view()


# 物体検出結果ページのビュー関数
def obj_result(request):
    return render(request, 'object_detection/result.html')

# セグメンテーション結果ページのビュー関数
def seg_result(request):
    return render(request, 'segmentation/result.html')

