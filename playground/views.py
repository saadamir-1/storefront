from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> response
# request handler
# action ( views is alse called action in some frameworks)


def say_hello(request, startYear, endYear, region):
    return HttpResponse(region)
