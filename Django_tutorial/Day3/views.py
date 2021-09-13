# I am the honour of this website --Dipesh Pandit

from django.http import HttpResponse
from django.shortcuts import render


def index(request):

    dic={"name":"Dipesh"}

    return render(request,'index.html',dic)


def about(request):


def contact(request):
    
