from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from pymongo import Connection
from models import Restaurant
from serializers import RestaurantSerializer
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
def login(request):
    #connect to our local mongodb
    db = MongoClient('localhost',27017)
    #get a connection to our database
    dbconn = db.restaurants
    loginCollection = dbconn['login']
    detailCollection = dbconn['detail']
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
        email = request.DATA["email"]
        password = request.DATA["password"]
        try:
            log=  dbconn.system_js.loginFunction(email,password)
            email =log[0]['email']
            name  =log[0]['name']
            gender  =log[0]['gender']
            address  =log[0]['address']
            role  =log[0]['role']
            phone  =log[0]['phone']
            id =log[0]['_id']
            a=str(id)
            detailCollection.insert({"id" :a ,"email" : email,"name":name,"phone":phone,"gender" :gender,"address":address,"role":role})
            print a
        except:
              return Response({ "false" })
        return Response({"id" :a,"role":role})

        
 