from django.shortcuts import render, get_object_or_404
from .forms import VideoForm
from .models import Video

def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            # フォームからタイトルを取得
            title = form.cleaned_data['title']
            
            # 同じタイトルのビデオが存在するか確認
            try:
                video = Video.objects.get(title=title)
                # 既存のビデオを更新
                video.video = form.cleaned_data['video']
                video.save()
            except Video.DoesNotExist:
                # 新しいビデオを保存
                form.save()

            return render(request, 'videoupload/upload_success.html')
    else:
        form = VideoForm()
    return render(request, 'videoupload/upload_video.html', {'form': form})

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'videoupload/video_list.html', {'videos': videos})
