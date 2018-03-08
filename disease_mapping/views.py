from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # return HttpResponse("diseases mapping index")
    context = {}
    return render(request, 'index.html', context)
