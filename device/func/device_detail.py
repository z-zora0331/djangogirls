# import json
from datetime import date, datetime, timedelta
import random
from . import base # 同一層目錄

def findProjectDict(input_ck):
    project_dict = {
        # "PK73Y2HHPK0MB7CSWR" : { "proj_id": 673, "proj_name": "18台南" },
        # "PKC50WAF5FA04BZWR9" : { "proj_id": 1075, "proj_name": "19台南" },
        # "PKWU4ZCBYTBAGGPTTH" : { "proj_id": 1207, "proj_name": "20台南" },
        "61a24e74-7a80-4f77-9fe3-08c0656578ee" : { "proj_id": 673, "proj_name": "18台南" },
        "33981437-4432-4dfa-8a0d-a59b37f6e7b8" : { "proj_id": 1075, "proj_name": "19台南" },
        "bc3cb244-14ab-420f-8a89-ee00f69ccc24" : { "proj_id": 1207, "proj_name": "20台南" },
    }

    dictfilt = lambda x : project_dict[x] == input_ck, project_dict[input_ck]
    return list(dictfilt)[1]

def findDeviceId(input_id, json_contents):
    # 取需要欄位做成字典查詢
    dev_dict = {}
    for dev in json_contents:
        dev_dict[dev['name']] = dev['id']

    # 查詢字典
    if dev_dict.get(input_id) is not None:
        return dev_dict[input_id]
    else:
        return None

def formatCounty(input_str):
    output_str = ""
    if input_str == "台中市":
        output_str = "臺中市"
    elif input_str == "台北市":
        output_str = "臺北市"
    elif input_str == "台南市":
        output_str = "臺南市"
    else:
        output_str = input_str
    return output_str

def findCountyCode(county, json_contents):
    for item in json_contents['countyItems']['countyItem']:
        if item['countyname'] == county:
            return item['countycode01']

def isNewDeviceId(device_id, json_contents):
    device_list = []
    for dev in json_contents:
        device_list.append(dev['id'])

    if device_id in device_list:
        return False
    else:
        return True

def randomId(obj, countycode, device_contents):
    for i in range(0, 100):
        random.seed(str(obj) + str(i) + str(random.random()))
        device_id = str(countycode) + str(int(random.random()*10000000))

        # 查設備id是不是新的(True/False)
        isNew = isNewDeviceId(device_id, device_contents)

        if isNew:
            return device_id

def findDeviceTypeKey(input_str):
    deviceType_dict = {
        22: "海域",
        24: "海灘",
        23: "地下水",
        20: "河川",
        21: "水庫",
        17: "異質資料(固定污染源)",
        13: "特殊性工業區(六輕大城)",
        19: "異質資料(氣象小時值)",
        15: "微型感測器",
        18: "異質資料(列管污染源)",
        25: "異質資料(鄉鎮天氣)",
        10: "國家級測站",
        11: "區域型測站(環保局)",
        14: "民間感測器",
        12: "大型事業(台電、中油)",
        16: "異質資料(車流)",
    }
    return list(filter(lambda x: deviceType_dict[x] == input_str, deviceType_dict))[0]

def findManufacturerKey(input_str):
    manufacturer_dict = {
        968: "jsene",
        426: "aeclpad",
    }
    return list(filter(lambda x: manufacturer_dict[x] == input_str, manufacturer_dict))[0]

def formatmsg(obj, device_contents):
    # obj縣市
    county = formatCounty(obj['county'])
    
    # 讀縣市代碼xml清單(gov開放API)
    # Sorce: https://api.nlsc.gov.tw/other/ListCounty
    county_contents = base.openFile(f"device/file/ListCounty.xml", "r", "xmltodict") ### xml轉換成json格式

    # 查縣市代碼 countycode(開頭不為0，金門、連江縣開頭為0，故轉換格式為int)
    countycode = int(findCountyCode(county, county_contents))

    # output
    data = {}
    data['id']             = randomId(obj, countycode, device_contents) # 流水號: 2024年起，縣市代碼 + 隨機7碼
    data['name']           = obj['id']
    data['desc']           = obj['desc']
    data['type']           = "general"
    data['uri']            = "" # R3G1XCXKHB7CR4BS
    data['lat']            = obj['lat']
    data['lon']            = obj['lon']
    data['alt']            = int(obj['alt'])
    if type(obj['attributes']) == list:
        data['attributes'] = obj['attributes']
    else:
        data['attributes'] = []
    data['updateTime']     = str(datetime.strptime(obj['time'], "%Y-%m-%d %H:%M:%S").date())
    data['reference']      = False
    data['display']        = True
    data['deviceType']     = str(findDeviceTypeKey(obj['deviceType'])) # 微型感測器 > 15
    data['ownerId']        = str(findManufacturerKey(obj['manufacturerId'])) # 426
    data['manufacturerId'] = obj['manufacturerId'] # aeclpad
    data['mobile']         = False
    data['outdoor']        = True
    data['tags']           = []
    data['county']         = county # 台南市>臺南市

    return data