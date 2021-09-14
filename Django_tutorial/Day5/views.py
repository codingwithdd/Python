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
    dtext=request.GET.get('text',"default")
    removepunc = request.GET.get('removepunc', "off")
    print(removepunc)
    if removepunc=="on":
        print(dtext)
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed_text=""
        for i in dtext:
            if i not in punctuations:
                analyzed_text=analyzed_text + i
        params={"purpose":"Removed Punctuations","analyze_text":analyzed_text}
        #Analyze the text

        return render(request,"analyze.html",params)
    else:
        return HttpResponse("Error")


def removepunc(request):

    return HttpResponse("Remove punc")

