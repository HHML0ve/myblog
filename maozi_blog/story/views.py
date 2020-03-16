from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def story(request):
    return HttpResponse('hello, this is second response')
