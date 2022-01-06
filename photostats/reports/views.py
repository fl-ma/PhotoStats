from django.shortcuts import render
from django.http import HttpResponse, HttpResponseServerError
from django.urls.conf import path


from images.models import Image

from .repFocalLengthDonut import FocalLengthDonut
from .repMobileVsCam import MobileVsCam

def index(request):
    
    action = request.GET.get('search')
    
    if not action:
        return init_view(request)
        
    elif action == 'Search':
        return plot_reports(request)
        
    else:
        #no idea
        return HttpResponseServerError("no action determined")   
    
    
def init_view(request):
    
    path_list = read_paths()
    
    return render(request, "reports/index.html",
                  context={'pathList': path_list,
                           }
                  )       
    
def plot_reports(request):
    path_list = read_paths()
    
    filter = selection_to_filter(request.GET.get('selected_path'))
    
    focalDonut = FocalLengthDonut(filter)
    
    mobileVsCam = MobileVsCam(filter)
    
    
    return render(request, "reports/index.html", 
                  context={'FocalLengthDonut_div': focalDonut.plot(), 
                            'CamerasOverTime_div': mobileVsCam.plot(),
                            'path_list': path_list
                           }
                  )
    
def selection_to_filter(input):
    return [['path',input]]

def read_paths():
    paths = Image.objects.values_list('path')
    path_list=[]
    
    for path in paths:
        #since SQLite does not support unique on field level
        if path[0] not in path_list:
            path_list.append(path[0])
            
    return path_list