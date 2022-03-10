from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def Home(request):
    context = {
        'req' : request
    }
    return render(request, "homePage.html", context)

def homework(request):
    context = {
        'req' : request
    }
    return render(request, "homework.html", context)