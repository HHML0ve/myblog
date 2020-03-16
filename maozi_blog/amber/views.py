from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def amber_main(request):
    return HttpResponse('Information for Amber')
