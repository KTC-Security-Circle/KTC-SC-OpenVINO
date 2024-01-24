from django import forms
from django.core.files.storage import default_storage
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator

class FileUploadSampleForm(forms.Form):
    file = forms.FileField(
        validators=[FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mov', 'wmv'])]
    )

    def save(self):
        """ファイルを保存するメソッド"""
        upload_file = self.cleaned_data['file']
        file_name = 'upload.mp4'

        # 同じ名前のファイルが存在する場合は削除
        if default_storage.exists('upload/' + file_name):
            default_storage.delete('upload/' + file_name)

        # 新しいファイルを保存
        saved_file_name = default_storage.save('upload/' + file_name, upload_file)
        return default_storage.url(saved_file_name)
