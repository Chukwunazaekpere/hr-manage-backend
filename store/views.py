from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView

from .serializers import AddToStore
from rest_framework.parsers import JSONParser

from django.http import JsonResponse
from .models import Store

class AddEmployee(CreateAPIView):
    serializer_class = AddToStore

    def AddEmployee(self, *args, **kwargs):
        data = JSONParser().parse(self.request)
        serializer = (data)
        if serializer.is_valid():
            print(serializer)
            serializer.save()
            return JsonResponse(serializer.data, 201)
        return JsonResponse(serializer.errors, 400)


class GetEmployees(ListAPIView):
    serializer_class = AddToStore
    queryset = Store.objects.all()

    def getEmployee(self, *args, **kwargs):
        return JsonResponse(self.queryset, 200)
    



