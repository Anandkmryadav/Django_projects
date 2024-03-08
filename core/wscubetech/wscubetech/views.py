from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render (request,"index.html")



def anand(request):
    return HttpResponse("Hello django!!")


def course(request):
    return HttpResponse("Hello course django!!")


