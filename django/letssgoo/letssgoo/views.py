from django.http import HttpResponse
from django.shortcuts import render


def home(request) :
    # return HttpResponse("Hello World . This is from Home")
    return render(request,"website/index.html")
def about(request) :
    return HttpResponse("Hello World . This is from about")

def contact(request) :
    return HttpResponse("Hello World . This is from contact ")


