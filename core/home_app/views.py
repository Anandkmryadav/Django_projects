from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def home(request):
    peoples = [
        {'name': 'Anand yadav','age' :26},
        {'name': 'Rohit Sharma','age' :23},
        {'name': 'Ankit kumar','age' :17},
        {'name': 'Abhishek kumar','age' :16},
        {'name': 'Sandeep ','age' :63},
    ]
    return render(request , "test.html" , context={"peoples" :peoples}) 
# sdfkgbsdfh