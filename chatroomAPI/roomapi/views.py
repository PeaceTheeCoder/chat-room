from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


import json

from roomapi.models import Message
# Create your views here.

@csrf_exempt
def index(request):
    if request.method == 'GET':
        try:
            message = Message.objects.all()
            arr =[]
            for x in message:  
                arr.append({'id':x.id, 'username':x.username, 'text':x.text, 'date':str(x.datetime)})
            response = json.dumps(arr)
        except:
            response =json.dumps([{'error':'0 Messages!'}])

    elif request.method == 'POST':
        payload = json.loads(request.body)
        user = payload[0]['username']
        message = payload[0]['text']
        
        rr = Message(username = user, text=message)
        try:
            rr.save()
            response =json.dumps([{'res':'message sent'}])
        except:
            response =json.dumps([{'res':'error sending a message'}])

    elif request.method == 'DELETE':
        payload = json.loads(request.body)
        print(payload)
        uid = payload[0]['id']
        message = Message.objects.get(pk=uid) 
        
        try:
            message.delete()
            response =json.dumps([{'res':'message deleted'}])
        except:
            response =json.dumps([{'arror','failed to deleted the message'}])

    elif request.method == 'PATCH':
        payload = json.loads(request.body)
        print(f"hello this {payload}")
        uid = payload[0]['id']
        text = payload[0]['text']
        message = Message.objects.get(pk=uid) 
        message.text = text
        try:
            message.save()
            response =json.dumps([{'res':'message updated'}])
        except:
            response =json.dumps([{'arror','failed to update the message'}])

    else:
        response =json.dumps([{'error':'bed request!!!'}])

    return HttpResponse(response,content_type="text/json")