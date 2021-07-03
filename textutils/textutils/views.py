#File Created by Paarth
from django.http import HttpResponse
from django.shortcuts import render


def index(request):

    return render(request,'index.html')

def removepunc(request):
    textdj=(request.GET.get("text",'default'))
    removepuncdj=(request.GET.get("removepunc",'default'))
    print(textdj)
    print(removepuncdj)
    # analysed=textdj
    punctuation='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analysed=""
    
    for char in textdj:
        if char not in punctuation:
            analysed=analysed+char
            

    params={"purpose":"remove punctuations","analysed_text":analysed}
    return render(request,'analyse.html',params)

