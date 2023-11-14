import json
import xmltodict

def openFile(filepath, mode, format_mode):
    with open(filepath, mode, encoding="utf-8") as file:
        contents = file.read()

        ### 轉換格式
        if format_mode == "json":
            contents = json.loads(contents)
        elif format_mode == "xmltodict":
            contents = xmltodict.parse(contents)

        return contents
