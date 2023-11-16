from django.http import JsonResponse
from django.http import HttpResponse
# from django.http import HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from device.func import device_detail, base
from rest_framework.views import APIView
import json

file_route = f"device/file/"

# Create your views here.
class deviceView(APIView):

    def get(request): # device_get
        try:
            # CK
            try:
                header = request.headers
                ck = header['Ck']
                project = device_detail.findProject(ck)
                device_json_path = file_route + str(project.split(',')[1]) + ".json"
            except:
                return JsonResponse({"status": False, "type": "request", "message": "error: CK"}, status=400)

            # 讀所有設備清單
            device_contents = base.openFile(device_json_path, "r", "json")

            # return
            return JsonResponse(device_contents, safe=False)
        except TypeError as e:
            return JsonResponse({"status": False, "type": "型別錯誤", "message": "error: "+str(e)}, status=400)
        except NameError as e:
            return JsonResponse({"status": False, "type": "未定義", "message": "error: "+str(e)}, status=400)
        except BaseException as e:
            return JsonResponse({"status": False, "type": "其他", "message": "error: "+str(e)}, status=400)

    def getId(request):
        try:
            # CK
            try:
                header = request.headers
                ck = header['Ck']
                project = device_detail.findProject(ck)
                device_json_path = file_route + str(project.split(',')[1]) + ".json"
            except:
                return JsonResponse({"status": False, "type": "request", "message": "error: CK"}, status=400)

            # Input body
            try:
                msg = request.body
                mqttmsg_str = msg.decode("utf-8")
                mqttmsg = json.loads(mqttmsg_str)
                msg_id  = mqttmsg['id']
            except:
                return JsonResponse({"status": False, "type": "request", "message": "error: body"}, status=400)

            # 讀所有設備清單
            device_contents = base.openFile(device_json_path, "r", "json")

            # 查設備id
            device_id = device_detail.findDeviceId(msg_id, device_contents)

            # return
            return HttpResponse(device_id)
        except TypeError as e:
            return JsonResponse({"status": False, "type": "型別錯誤", "message": "error: "+str(e)}, status=400)
        except NameError as e:
            return JsonResponse({"status": False, "type": "未定義", "message": "error: "+str(e)}, status=400)
        except BaseException as e:
            return JsonResponse({"status": False, "type": "其他", "message": "error: "+str(e)}, status=400)

    @csrf_exempt
    def post(request):
        try:
            # CK
            try:
                header = request.headers
                ck = header['Ck']
                project = device_detail.findProject(ck)
                device_json_path = file_route + str(project.split(',')[1]) + ".json"
            except:
                return JsonResponse({"status": False, "type": "request", "message": "error: CK"}, status=400)

            # Input body
            try:
                msg = request.body
                mqttmsg_str = msg.decode("utf-8")
                mqttmsg = json.loads(mqttmsg_str)
                msg_id  = mqttmsg['id']
            except:
                return JsonResponse({"status": False, "type": "request", "message": "error: body"}, status=400)

            # 讀所有設備清單
            device_contents = base.openFile(device_json_path, "r", "json")

            # 查設備id
            device_id = device_detail.findDeviceId(msg_id, device_contents)

            # Insert
            if device_id is None:
                # format
                new_data = device_detail.formatmsg(mqttmsg, device_contents)

                # 寫入所有設備清單中
                with open(device_json_path, "w+", encoding="utf-8") as file:
                    device_contents.append(new_data)
                    file.write(json.dumps(device_contents, ensure_ascii=False, indent=4))
                    file.close()

                return JsonResponse(new_data, safe=False)
            else:
                return JsonResponse({"status": True, "type": "info", "message": "device id is exist."})

        except TypeError as e:
            return JsonResponse({"status": False, "type": "型別錯誤", "message": "error: "+str(e)}, status=400)
        except NameError as e:
            return JsonResponse({"status": False, "type": "未定義", "message": "error: "+str(e)}, status=400)
        except BaseException as e:
            return JsonResponse({"status": False, "type": "其他", "message": "error: "+str(e)}, status=400)
