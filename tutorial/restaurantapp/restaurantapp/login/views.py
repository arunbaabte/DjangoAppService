from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from pymongo import Connection
from models import sign
from serializers import signSerializer
import json
from pymongo import MongoClient
from django.conf import settings
from django.http import HttpResponse
from django.http import HttpResponseRedirect, HttpResponse
from rest_framework.parsers import JSONParser
from bson import Binary, Code
from bson.json_util import dumps
@csrf_exempt

@csrf_exempt
@api_view(['GET','POST'])
def signs(request):
    #connect to our local mongodb
    db = MongoClient('localhost',27017)
    #get a connection to our database
    dbconn = db.restaurants
    loginCollection = dbconn['signs']
    if request.method == 'GET':

        signs = []
        for r in loginCollection.find():
            signs = sign(r["email"],r["password"])
            print signs
            # signs.append(signs)
        # serializedList = signSerializer(signs, many=True)
        return Response("hi")
    elif request.method == 'POST':
        #get data from the request and insert the record
        email = request.DATA["email"]
        password = request.DATA["password"]
        try:
            log=  dbconn.system_js.signFunction(email,password)
        except:
             return Response({ "ok": "false" })
        return Response({"success"})
