from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1> this is the musik home page</h1>")