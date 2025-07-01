from django.shortcuts import render
from django.http import JsonResponse 
from .models import Customer

# Create your views here.
def customer_list(request): 
    data = list(Customer.objects.values()) 
    return JsonResponse(data, safe=False) 