from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    """Declare my home page"""
    return HttpResponse("Hello friend, you are at the poll index")

