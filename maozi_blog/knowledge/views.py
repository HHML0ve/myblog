from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def knowledge(request):
    return HttpResponse('I am a summary')


def catalog(request):
    return HttpResponse('I am catalog')
