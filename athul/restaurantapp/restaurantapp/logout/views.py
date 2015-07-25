from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

import json
from pymongo import MongoClient
from django.conf import settings
from django.http import HttpResponse
from django.http import HttpResponseRedirect, HttpResponse
from rest_framework.parsers import JSONParser
from bson import Binary, Code
from bson.json_util import dumps
from bson.objectid import ObjectId
from bson import ObjectId

@csrf_exempt

@csrf_exempt
@api_view(['GET','POST'])
def logout(request):
    #connect to our local mongodb
    db = MongoClient('localhost',27017)
    #get a connection to our database
    dbconn = db.restaurants

    detailCollection = dbconn['detail']
    if request.method == 'GET':
        login = []
        for r in detailCollection.find():
        #     logins = Restaurant(r["email"],r["password"])
        #     print logins
        #     # login.append(logins)
        # # serializedList = RestaurantSerializer(login, many=True)
         return Response("hi")
    elif request.method == 'POST':
        #get data from the request and insert the record
        id = request.DATA["id"]
        print id
        try:
            # detailCollection.remove({"id" :id})
            dbconn.system_js.logout(id)
        except:
              return Response({ "false" })
        return Response({"true"})

        
 