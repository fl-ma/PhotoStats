from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse, HttpResponseServerError

from .models import Directory
from .directoryTreeUi import DirectoryTreeUi


class ListAllView(generic.ListView):
    model = Directory


def tree(request):

    uiTree = DirectoryTreeUi(request)

    return HttpResponse(uiTree.render())
