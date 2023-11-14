# Heroku

[安裝] 
    1. Heroku
    https://devcenter.heroku.com/articles/getting-started-with-python#set-up

    2. 軟體套件
    $ pip install dj-database-url gunicorn whitenoise

    3. gunicorn mysite.wsgi => 出現錯誤: No module named 'fcntl'
    $ 微軟是改使用 python manage.py runserver
    Heroku文件: https://devcenter.heroku.com/articles/getting-started-with-python#define-a-procfile
    

[告訴Heroku需要在我們的伺服器上安裝哪些Python套件]
    $ pip freeze > requirements.txt

[程式變動之Mark]
    ### Heroku註解
    ### Heroku新增

## 執行
    ‧[命令提示字元] 位置：C:\Users\JingYa.Zeng>
    
[登入Heroku]
    $ heroku login     [按任意鍵會跳出網頁登入]
    $ heroku login -i  [輸入帳號密碼]
    看到Logged in as XXXXX@gmail.com 代表成功
    
[建立專案]
    $ heroku create XXXXX
    $ heroku create djangogirlsblog [此專案]

    ‧[需要新增信用卡]
    Creating ⬢ djangogirlsblog... !
    !    To create an app, verify your account by adding payment information. Verify now at https://heroku.com/verify Learn more at https://devcenter.heroku.com/articles/account-verification
    
[下載heroku-push外掛]
    $ heroku plugins:install https://github.com/ddollar/heroku-push

    ‧[下載失敗]
    Installing plugin https://github.com/ddollar/heroku-push... failed
    Error: no name in C:\Users\JingYa.Zeng\AppData\Local\heroku\package.json