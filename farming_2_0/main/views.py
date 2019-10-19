from django.http import JsonResponse
from main.models import Crop,Stage,Machine

def GetCrops(request):
    data = []
    for crop in list(Crop.objects.all()):
        data.append({"name": crop.name,
                     "image":crop.image, "id":crop.cid})
    return JsonResponse(data, content_type='application/json', safe=False)

def GetStages(request,crop_id):
    data = {}
    for stage in list(Crop.objects.get(cid=crop_id).stages.all()):
        data[stage.name] = {"image":stage.image,"sid":stage.sid}
    return JsonResponse(data, content_type='application/json')

def GetMachines(request,stage_id):
    data = {}
    for machine in list(Stage.objects.get(sid=stage_id).machines.all()):
        data[machine.name] = {"rent": machine.rent,"details":machine.details,"mid":machine.mid, "image":machine.image}
    return JsonResponse(data, content_type='application/json')
