from django.shortcuts import render

# Create your views here.
def all_chai(requests ):
    return render(requests,"chai/all_chai.html")