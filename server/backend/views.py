from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def home(request):
    return HttpResponse("DBMS Project 2021")


def projectid(request):
    return HttpResponse("015248")


def projectname(request):
    return HttpResponse("DBMS LAB CSE SEM5 ")

def fest(request):
    return HttpResponse("DBMS Class Tommorrow")

def meal(request):
    return HttpResponse("D3 MEals a Day")


