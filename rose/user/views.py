from django.shortcuts import render
from django.http import JsonResponse
import json

from user.models import User #추가

def login(request):
    if request.method == 'POST':
        data=json.loads(request.body)
        email = data['email']
        password = data['password']

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None 
        
        if user == None:
            return JsonResponse({'result': False})
        else:
            username = email.split('@')[0] 
            return JsonResponse({'result': True, 'id': username})

def register(request):
    if request.method == 'POST':
        data=json.loads(request.body)
        email = data['email']
        password = data['password']
        password2 = data['password2']

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None 
        
        if user == None and password == password2:
            #유저를 만든다.
            username = email.split('@')[0] 
            user = User(email = email, password = password, username = username)
            user.save()
            return JsonResponse({'result': True, 'id': username})            
        else:
            return JsonResponse({'result': False})
