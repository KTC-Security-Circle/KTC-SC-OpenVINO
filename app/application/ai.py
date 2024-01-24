import shutil
import os
import time

def run():
    # 元のファイルパス
    original_file = os.path.join('media', 'upload', 'upload.mp4')

    # 新しいファイル名
    new_file = os.path.join('media', 'upload', 'reupload.mp4')

    # ファイルが存在するか確認
    if os.path.exists(original_file):
        # 元のファイルを新しいファイル名でコピー
        shutil.copy2(original_file, new_file)
        print('3')
        # 3秒間待機
        time.sleep(3)

        return "ファイルが複製され、3秒間待機しました。"
    else:
        print('エラー')
        return "元のファイルが見つかりません。"
