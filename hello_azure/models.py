from django.db import models
from django.core.validators import FileExtensionValidator


class Video(models.Model):
    file = models.FileField(upload_to='videos/')

class VideoTest(models.Model):
    attach = models.FileField(
        upload_to='uploads/%Y/%m/%d/',
        validators=[FileExtensionValidator(['mp4', ])],
    )