from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("welcomme application !!!")
# Create your views here.
