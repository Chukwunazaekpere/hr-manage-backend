from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView

from .serializers import AddToStore
from rest_framework.parsers import JSONParser

from django.http import JsonResponse
from .models import Store
from pymongo import MongoClient
import json
from bson import json_util


class AddEmployee(CreateAPIView):
    serializer_class = AddToStore

    def post(self, *args, **kwargs):
        print("\n\n\t Locating DB server...")
        client = MongoClient("mongodb://Chukwunazaekpere:Chukwunazaekpere5777@hr-shard-00-00.cu4aa.mongodb.net:27017,hr-shard-00-01.cu4aa.mongodb.net:27017,hr-shard-00-02.cu4aa.mongodb.net:27017/HR-management?ssl=true&replicaSet=atlas-1hk3kc-shard-0&authSource=admin&retryWrites=true&w=majority")
        database = client.get_database("HR-Management")
        employees = database.Employees

        data = self.request.data
        print("Computing data...")
        employees.insert(data)
        print("\n\n\t Document saved...")

        print("Done...")
        return Response(data, 200)


class GetEmployees(ListAPIView):
    serializer_class = AddToStore
    queryset = Store.objects.all()

    def get(self, *args, **kwargs):
        client = MongoClient("mongodb://Chukwunazaekpere:Chukwunazaekpere5777@hr-shard-00-00.cu4aa.mongodb.net:27017,hr-shard-00-01.cu4aa.mongodb.net:27017,hr-shard-00-02.cu4aa.mongodb.net:27017/HR-management?ssl=true&replicaSet=atlas-1hk3kc-shard-0&authSource=admin&retryWrites=true&w=majority")
        database = client.get_database('HR-Management')
        employees = database.Employees 
        employees = list(employees.find())
        data = json.loads(json_util.dumps(employees))
        return Response(data, 200, {'Content-Type': 'applicatio/json'})
    



