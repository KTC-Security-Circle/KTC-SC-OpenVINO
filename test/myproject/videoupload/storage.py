# videoupload/storage.py
from django.core.files.storage import FileSystemStorage
import os

class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        # ファイルが既に存在する場合は、それを削除します
        if self.exists(name):
            os.remove(os.path.join(self.location, name))
        return name
