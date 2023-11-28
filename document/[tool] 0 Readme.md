[官方網站](https://docs.djangoproject.com/en/4.2/)
[Getting started with Django](https://www.djangoproject.com/start/)

1. https://carolhsu.gitbooks.io/django-girls-tutorial-traditional-chiness/content/index.html <done>
   https://tutorial.djangogirls.org/en/ <done 兩個版本很像，應是新舊版差別>
   https://tutorial.djangogirls.org/en/whats_next/ <ing 最後一頁----後續>
   https://tutorial-extensions.djangogirls.org/en/ <ing 後續>
2. https://djangogirlstaipei.gitbooks.io/django-girls-taipei-tutorial/content/ <中文版的文件>
   https://djangogirlstaipei.gitbooks.io/django-girls-taipei-tutorial/content/django/deploy.html
3. [How to Deploy a Django App on Render](https://www.freecodecamp.org/news/deploying-a-django-app-to-render/)
4. https://github.com/JacquesBlazor/python.DjangoTutorial.zh-tw
5. https://docs.djangoproject.com/zh-hans/4.2/ <官方教程>
6. https://docs.djangoproject.com/en/3.2/intro/tutorial01/ <官方教程>
7. https://thekennethlove.com/ <girls Django入門影片課程>
8. https://www.coursera.org/specializations/django <girls Django一些視訊講座可以免費旁聽>
9. https://www.codecademy.com/learn/learn-python <codecademy Python課程>
10. https://yhhuang1966.blogspot.com/2020/11/python-django-3_29.html
11. https://ithelp.ithome.com.tw/articles/10212364
12. https://summer10920.github.io/2020/03-11/css-baseclass-3/ <css>

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
    $ python manage.py migrate [新版，依據INSTALLED_APPS配置]

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
    $ python manage.py makemigrations blog [建立遷移-新增model]
    $ python manage.py migrate blog [執行遷移-新增DB表格] 表格命名:AppName_className，例如:blog_post、blog_comment
    $ python manage.py showmigrations [查看所有遷移]

[刪除application]
    $ python manage.py migrate xxx zero [刪除models.py]
    ‧刪除 xxx 文件夾
    ‧刪除 settings.py 的 INSTALLED_APPS 相關app
    ‧刪除 urls.py 相關app內容

[安裝套件]
    $ pip install XXX
    - django
    - djangorestframework
    - xmltodict
