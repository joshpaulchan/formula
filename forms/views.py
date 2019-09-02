from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("Hello")


def submit_form(request, form_id):
    return HttpResponse(form_id)
