from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('add-employee/', views.AddEmployee.as_view(), name='add-employee'),
    path('get-employees/', views.GetEmployees.as_view(), name='get-employees'),
]

