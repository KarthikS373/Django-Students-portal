from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def Home(request):
    context = {
        'req' : request
    }
    return render(request, "dashboard.html", context)