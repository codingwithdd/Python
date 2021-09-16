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
    dtext= request.GET.get('text',"default")
    removepunc = request.GET.get('removepunc', "off")
    upper = request.GET.get('upper', "off")
    lower = request.GET.get('lower', "off")
    extraspace = request.GET.get('extraspace', "off")
    chcount = request.GET.get('chcount', "off")

    print(removepunc)
    if removepunc=="on":
        print(dtext)
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        remove_punc=""
        for i in dtext:
            if i not in punctuations:
                remove_punc=remove_punc + i
        params={"purpose":"Removed Punctuations","analyze_text":remove_punc}
        #Analyze the text
        return render(request,"analyze.html",params)

    elif(upper=="on"):
        upper_text = ""
        for i in dtext:
            upper_text=upper_text + i.upper()
        params={"purpose":"Changed to Upper case","analyze_text":upper_text}
        return render(request, "analyze.html", params)

    elif(lower =="on"):
        lower_text = ""
        for i in dtext:
            lower_text = lower_text + i.lower()
        params = {"purpose": "Changed to Lower case", "analyze_text": lower_text}
        return render(request, "analyze.html", params)

    elif (extraspace == "on"):
        extra_space = ""
        for index,i in enumerate(dtext):
            if not (dtext[index]==" " and dtext[index+1]==" "):
                extra_space=extra_space+i
        params = {"purpose": "Removed extra space", "analyze_text": extra_space}
        return render(request, "analyze.html", params)

    elif (chcount == "on"):
        ch_count=int(0)
        for i in dtext:
            ch_count=ch_count+1
        params = {"purpose": "count character", "analyze_text": ch_count}
        return render(request, "analyze.html", params)

    else:
        return HttpResponse("Error")

def removepunc(request):

    return HttpResponse("Remove punc")

def about(request):

    return render(request,'about.html')

