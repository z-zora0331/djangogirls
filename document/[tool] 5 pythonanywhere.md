# pythonanywhere

‧註冊：https://www.pythonanywhere.com/
‧Account/API token

‧Bash
    $ git clone https://github.com/z-zora0331/djangogirls.git
    $ cd djangogirls/
    $ pip3.8 install --user pythonanywhere
    $ pip install djangorestframework

    $ python manage.py migrate => 將DB改成sqlite3 (在pythonanywhere的PostgreSQL需要付費)
    $ python manage.py createsuperuser

    ‧使: zora0331
    ‧帳: zx096731@gmail.com
    ‧密: password

    $ ls
    README.md  blog  db.sqlite3  document  manage.py  mysite  package-lock.json  requirements.txt  runtime.txt  static

‧Web
    Add a new web app

    Code:
    ‧Source code: /home/zora0331/djangogirls
    ‧Working directory: /home/zora0331/
    ‧WSGI configuration file: /var/www/zora0331_pythonanywhere_com_wsgi.py

    Static files:
    /static/    /home/zora0331/djangogirls/static
