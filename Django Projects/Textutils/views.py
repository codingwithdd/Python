from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    dtext= request.POST.get('text',"default")
    removepunc = request.POST.get('removepunc', "off")
    upper = request.POST.get('upper', "off")
    lower = request.POST.get('lower', "off")
    extraspace = request.POST.get('extraspace', "off")
    chcount = request.POST.get('chcount', "off")

    if removepunc=="on":
        print(dtext)
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        remove_punc=""
        for i in dtext:
            if i not in punctuations:
                remove_punc=remove_punc + i
        params={"purpose":"Removed Punctuations","analyze_text":remove_punc}
        dtext=remove_punc

    if(lower =="on"):
        lower_text = ""
        for i in dtext:
            lower_text = lower_text + i.lower()
        params = {"purpose": "Changed to Lower case", "analyze_text": lower_text}
        dtext=lower_text

    if (extraspace == "on"):
        extra_space = ""
        for index,i in enumerate(dtext):
            if not (dtext[index]==" " and dtext[index+1]==" "):
                extra_space=extra_space+i
        params = {"purpose": "Removed extra space", "analyze_text": extra_space}

    if (removepunc!="on" and lower !="on" and extraspace != "on"):
        return HttpResponse("Select option      ")

    return render(request, "analyze.html", params)

def removepunc(request):

    return HttpResponse("Remove punc")

def about(request):

    return render(request,'about.html')

