from django.http import HTTPResponse
from django.shortcuts import render

# Create your views here.


def index(req):
    return HTTPResponse("Onememos~ Hello, World~^.~")
