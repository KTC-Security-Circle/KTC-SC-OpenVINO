# OpenVINO ローカルアプリ

## 概要
- このアプリは、INTELのOpenVINOを使用した、Djangoアプリケーションです。
- プロジェクトは、ローカル環境でのOpenVINOデモを簡単に行えるようにしたものです。
- 現在は物体検出動画デモのみ対応しています。

## 動作環境

まずIntel CPUを搭載したパソコンにpythonが必要です

--動作確認済み環境--
- 第 6 世代から第 13 世代の インテル® Core™ プロセッサー
- Windows10,11

--公式引用システム要求--
- 第6世代から第13世代のインテル® Core™ プロセッサー
- インテル® Core™ ウルトラ プロセッサー
- 第 1 世代から第 4 世代までのインテル® Xeon® スケーラブル プロセッサー
- Arm* および Arm64 CPU
- Apple* M1 および M2
- ラズベリーパイ*

--互換性のあるオペレーティング システム--
- Ubuntu* 22.04 長期サポート (LTS)、64 ビット (カーネル 5.15+)
- Ubuntu 20.04 LTS、64 ビット (カーネル 5.15 以降)
- Ubuntu 18.04 LTS (制限付き)、64 ビット (カーネル 5.4 以降)
- Windows® 10および11
- macOS* 10.15 以降、64 ビット
- macOS* 11 以降、Arm64
- Red Hat* Enterprise Linux* 8、64 ビット
- Debian* 9、Arm64、および Arm
- CentOS* 7 64 ビット

## セットアップ手順
1. リポジトリのクローン
```shell
git clone https://github.com/KTC-Security-Circle/KTC-SC-OpenVINO.git
```

2. アプリケーション フォルダーに移動
```shell
cd KTC-SC-OpenVINO
```

3. アプリの仮想環境を作成
```shell
py -m venv .venv
.venv\scripts\activate
python.exe -m pip install --upgrade pip
```

4. 依存関係のインストール
```shell
pip install -r requirements.txt
``` 

5. セットアップ手順
```shell
python manage.py makemigrations
python manage.py migrate  
```

6. アプリを実行
```shell
python manage.py runserver

```
7. ブラウザでアクセス
http://localhost:8000 
