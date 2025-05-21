from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hydjobs(request):
    s="<h1> welcome to hyderabad jobs </h1>"
    return HttpResponse(s)

def bangjobs(request):
    s="<h1> welcome to Bang jobs </h1>"
    return HttpResponse(s)

def punejobs(request):
    s="<h1> welcome to pune jobs </h1>"
    return HttpResponse(s)

def chennaijobs(request):
    s="<h1> welcome to chennai jobs </h1>"
    return HttpResponse(s)
