from django.shortcuts import render 
from django.http import HttpResponse, request

# Create your views here.
def Login(request):
    return HttpResponse('Login')

def Register(request):
    return HttpResponse('Register')