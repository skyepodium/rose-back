from django.shortcuts import render
from django.http import JsonResponse
import json
# Create your views here.


def login(request):
    if request.method == 'POST':
        print(request.body)
        data=json.loads(request.body)
        id = data['id']
        password = data['password']
        print(id + ' ' + password)
        return JsonResponse({'foo':'bar'})