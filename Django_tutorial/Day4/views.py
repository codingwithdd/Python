# I am the honour of this website --Dipesh Pandit

from django.http import HttpResponse
from django.shortcuts import render


def index(request):

    # dic={"name":"Dipesh"}

    return render(request,'index.html')

#
# def about(request):
#     return



def analyze(request):
    #get the text
    dtext=print(request.GET.get('text',"default"))
    print(dtext)
    #Analyze the text
    return HttpResponse("welcome to Analyze")

