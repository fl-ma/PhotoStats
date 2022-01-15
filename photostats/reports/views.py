from django.shortcuts import render
from django.http import HttpResponse, HttpResponseServerError
from django.urls.conf import path
from django.template import loader

from .repTimelines import RepTimelines
from .repCompare import RepCompare

def index(request):
    
    template = loader.get_template('reports/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def timelines(request):
    
    try:
        report = RepTimelines(request)
        
        return report.render()        
        
    except Exception as inst:
        text = str(inst)
        return HttpResponseServerError(text)
    
    
def compare(request):
    
    try:
        report = RepCompare(request)
        
        return report.render()        
        
    except Exception as inst:
        text = str(inst)
        return HttpResponseServerError(text) 
