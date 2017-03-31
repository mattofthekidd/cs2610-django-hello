from django.shortcuts import render
from django.http import HttpResponse
import time
import PageCount

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. </br>time: " + time.strftime("%c") + "</br> ")