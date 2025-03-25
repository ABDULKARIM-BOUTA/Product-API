from django.shortcuts import render
from django.http import JsonResponse
import json

def api_home(request, *args, **kwargs):
    print(request.GET)

    body = request.body
    data = {}

    try:
        data = json.loads(body)
    except:
        pass

    print(request.POST)
    #print(data.keys())
    return JsonResponse(data)