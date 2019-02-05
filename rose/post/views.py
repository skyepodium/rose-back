from django.shortcuts import render
from django.http import JsonResponse
import json

from django.core import serializers

from user.models import User #추가
from post.models import Post

def postSave(request):
    if request.method == 'POST':
        data=json.loads(request.body)
        username = data['id']
        contents = data['contents']
        print(username)
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None 

        if user == None:
            return JsonResponse({'result': False})
        else:
            post = Post(writer = user, contents = contents, username=username)
            post.save()

            return JsonResponse({'result': True})

def postGet(request):
    if request.method == 'GET':
        posts = Post.objects.values().all().order_by('-id')
        ret = dict()
        ret['result'] = True
        ret['list'] = list(posts)
        return JsonResponse(ret, safe=False)