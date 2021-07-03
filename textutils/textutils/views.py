#File Created by Paarth
from django.http import HttpResponse
from django.shortcuts import render


def index(request):

    return render(request,'index.html')



def analyse(request):
    textdj=(request.GET.get("text",'default'))
    removepunc=request.GET.get("removepunc",'off')
    uppercase=request.GET.get("uppercase",'off')
   
    #Remove Punctuation
    analysed=""
    analysed1=""

    if removepunc == 'on': 
        punctuation='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in textdj:
            if char not in punctuation:
                analysed= analysed + char
                params = {"purpose1":"remove punctuations","analysed_text":analysed}


    
    if uppercase == 'on':
        for char in textdj:
            analysed1 = analysed1 + char.upper()
            params = {"purpose":"uppercase","op":analysed1}

    
    return render(request,"analyse.html",params)

    





    




