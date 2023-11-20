# EnterpriseDB 的 PostgreSQL

[安裝]
    ‧安裝網址：http://www.enterprisedb.com/products-services-training/pgdownload#windows
    ‧安裝步驟：https://www.postgresqltutorial.com/postgresql-getting-started/install-postgresql/

    ‧安裝位置：C:\Program Files\PostgreSQL\16
    ‧Data Directory: C:\Program Files\PostgreSQL\16\data

    ‧超級使用者: postgres
    ‧密碼: password
    ‧預設連接埠: 5432

    ‧設定環境變數：C:\Program Files\PostgreSQL\16\bin

[說明文件]
    ‧https://docs.postgresql.tw/ <繁中>

[操作]
    ‧建立使用者
    # CREATE USER postgres;

    ‧建立資料庫
    # CREATE DATABASE djangogirls OWNER postgres;

    ‧更新DATABASES [mysite/settings.py]
    ‧下載 PostgreSQL package for Python
    $ pip install psycopg2

    ‧設定
    $ python manage.py migrate
    $ python manage.py createsuperuser --username postgres
        ‧使: postgres
        ‧帳: zx096731@gmail.com
        ‧密: password