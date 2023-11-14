[官方網站](https://docs.djangoproject.com/en/4.2/)
[Getting started with Django](https://www.djangoproject.com/start/)

1. https://carolhsu.gitbooks.io/django-girls-tutorial-traditional-chiness/content/index.html <進行中>
   https://tutorial.djangogirls.org/en/
   https://tutorial-extensions.djangogirls.org/en/ <後續>
2. https://djangogirlstaipei.gitbooks.io/django-girls-taipei-tutorial/content/
3. [How to Deploy a Django App on Render](https://www.freecodecamp.org/news/deploying-a-django-app-to-render/)

# Start

[網址]
    ‧admin登入 http://127.0.0.1:8000/admin/login/?next=/admin/

[pip指令]
    $ pip list [查詢目前下載套件的版本]

[虛擬環境myvenv]
    $ C:/Users/JingYa.Zeng/Anaconda3/envs/work/python.exe -m venv myvenv [建立環境，第一次]
    $ myvenv\Scripts\activate [啟動環境]
    $ deactivate [關閉虛擬環境]

    ‧路徑: C:\Users\JingYa.Zeng\djangogirls
    ‧(原本) PS C:\Users\JingYa.Zeng\djangogirls>
    ‧(新的) (myvenv) PS C:\Users\JingYa.Zeng\djangogirls>

[建立專案mysite]
    $ django-admin.exe startproject mysite

[設定SQLite資料庫]
    $ python manage.py syncdb [舊版]
    $ python manage.py migrate [新版]

    ‧VScode可下載套件，SQLite Viewer

[建立超級使用者]
    $ python .\manage.py createsuperuser
    
    ‧使: jingya.zeng
    ‧帳: zx096731@gmail.com
    ‧密: password

[運行專案，啟動WebServer]
    $ cd .\mysite\
    $ python manage.py runserver

[建立application]
    $ python manage.py startapp blog [建立APP]
    $ python manage.py makemigrations blog [建立DB:blog_post]

[安裝套件]
    $ pip install XXX