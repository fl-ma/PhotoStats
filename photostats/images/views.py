from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views import generic

from .models import Image


class ListAllView(generic.ListView):
    model = Image
