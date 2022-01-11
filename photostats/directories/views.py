from django.shortcuts import render
from django.views import generic

from .models import Directory


class ListAllView(generic.ListView):
    model = Directory
