from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the importer index.")


def action(request):
    return HttpResponse("Hello, world. You're at the importer action.")