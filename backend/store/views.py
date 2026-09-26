from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    data = {
        'message': 'Welcome to the E-commerce Store!',
    }
    return JsonResponse(data)