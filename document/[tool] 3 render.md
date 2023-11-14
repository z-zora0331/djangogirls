# Render

取代Heroku

[官方文件](https://render.com/docs/deploy-django)

參考文章
https://medium.com/@bear817005/heroku-%E7%B5%82%E6%AD%A2%E5%85%8D%E8%B2%BB-%E9%81%B7%E7%A7%BB%E5%88%B0-render-cloud-%E4%B9%8B%E7%B4%80%E9%8C%84-a81395495669

[安裝]

    1. pipx
    $ python3 -m pip install --user pipx

    2. poetry
    ※ [pip 替代方案選擇——Pipenv vs Poetry](https://blog.kyomind.tw/python-poetry/#Poetry-%E6%98%AF%E4%BB%80%E9%BA%BC%EF%BC%9F)
    $ (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python

    3. 設定環境變數
    %APPDATA%\Python\Scripts

    4. 查詢是否安裝成功
    $ poetry --version
    ※ Poetry (version 1.7.0)

## 執行