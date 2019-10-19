from django.http import JsonResponse
from main.models import Crop,Stage,Machine

def GetCrops(request):
    data = []
    for crop in list(Crop.objects.all()):
        data.append({"name": crop.name,
                     "image": crop.image, "id": crop.cid})
    return JsonResponse(data, content_type='application/json', safe=False)


def GetStages(request, crop_id):
    data = []
    for stage in list(Crop.objects.get(cid=crop_id).stages.all()):
        data.append({'name': stage.name,
                     "image":stage.image,
                     "id":stage.sid})
    return JsonResponse(data, content_type='application/json', safe=False)

def GetMachines(request,stage_id):
    data = []
    for machine in list(Stage.objects.get(sid=stage_id).machines.all()):
        data.append({"rent": machine.rent,"details":machine.details,"id":machine.mid, "image":machine.image,
                     'name': machine.name})
    return JsonResponse(data, content_type='application/json',
                        safe=False)
