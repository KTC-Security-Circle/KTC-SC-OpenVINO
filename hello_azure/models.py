from django.db import models
from .storage import OverwriteStorage

def video_directory_path(instance, filename):
    # 新しいファイル名を生成（例: 'uploaded_video.mp4'）
    return 'videos/uploaded_video.mp4'

class Video(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to=video_directory_path, storage=OverwriteStorage())
