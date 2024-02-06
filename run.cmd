cd .\KTC-SC-OpenVINO\
python -m venv .venv
call .venv\Scripts\activate
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py makemigrations 
python manage.py migrate  
start /b python manage.py runserver

cd ..
cd .\Electron\

timeout /t 6
npx electron main.js

echo DjangoサーバーとElectronアプリケーションが起動しました。

pause
