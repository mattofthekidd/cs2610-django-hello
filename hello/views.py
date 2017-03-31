from django.shortcuts import render
from django.http import HttpResponse
import time
from .models import PageCount

# Create your views here.
def index(request):
    # get row from database
    row, create = PageCount.objects.get_or_create(page='index')
    # increment by one
    row.count += 1
    # save the value
    row.save()
    return HttpResponse("Hello, world. </br>time: " + time.strftime("%c") + "</br>visisted #" + str(row.count)) 