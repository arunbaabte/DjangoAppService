from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from pymongo import Connection

import json
from pymongo import MongoClient
from django.conf import settings
from django.http import HttpResponse
from django.http import HttpResponseRedirect, HttpResponse

@csrf_exempt

@csrf_exempt
@api_view(['GET','POST'])
def home(request):
    #connect to our local mongodb
    db = MongoClient('localhost',27017)
    #get a connection to our database
    dbconn = db.restaurants
    loginCollection = dbconn['detail']
    if request.method == 'GET':

        login = []
        for r in loginCollection.find():
        #     logins = Restaurant(r["email"],r["password"])
        #     print logins
        #     # login.append(logins)
        # # serializedList = RestaurantSerializer(login, many=True)
         return Response("hi")
    elif request.method == 'POST':
        #get data from the request and insert the record
        id = request.DATA["email"]
        print id
        try:
            log = loginCollection.find({"id":id})
            
            id =log[0]['name']
            print id
        except:
              return Response({ "false" })
        return Response({id})

        
 