from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView

from .serializers import AddToStore
from rest_framework.parsers import JSONParser

from django.http import JsonResponse
from .models import Store
from pymongo import MongoClient


class AddEmployee(CreateAPIView):
    serializer_class = AddToStore

    def post(self, *args, **kwargs):
        client = MongoClient("mongodb://Chukwunazaekpere:Chukwunazaekpere5777@hr-shard-00-00.cu4aa.mongodb.net:27017,hr-shard-00-01.cu4aa.mongodb.net:27017,hr-shard-00-02.cu4aa.mongodb.net:27017/HR-management?ssl=true&replicaSet=atlas-1hk3kc-shard-0&authSource=admin&retryWrites=true&w=majority")
        database = client.get_database("HR-Management")
        employees = database["Employees"]

        print(*args, **kwargs)
        print('\n\tData: ', self.request.data)
        employees.insert_one(self.request.data)
        serializer = (self.request.data)

        return JsonResponse(serializer.data, 201)


class GetEmployees(ListAPIView):
    serializer_class = AddToStore

    def getEmployee(self, *args, **kwargs):
        client = MongoClient("mongodb://Chukwunazaekpere:Chukwunazaekpere5777@hr-shard-00-00.cu4aa.mongodb.net:27017,hr-shard-00-01.cu4aa.mongodb.net:27017,hr-shard-00-02.cu4aa.mongodb.net:27017/HR-management?ssl=true&replicaSet=atlas-1hk3kc-shard-0&authSource=admin&retryWrites=true&w=majority")
        database = client.get_database('HR-Management')
        employees = database['Employees']

        return JsonResponse(employees, 200)
    



