from django.shortcuts import render
from django.http import HttpResponse, HttpResponseServerError
from django.urls.conf import path
from django.template import loader


from images.models import Image
from directories.models import Directory
from directories.directoryTree import get_directory_tree_list, selection_to_filter

from .repFocalLengthDonut import FocalLengthDonut
from .repMobileVsCam import MobileVsCam
from .repMobileVsCamRatio import MobileVsCamRatio


def index(request):
    
    template = loader.get_template('reports/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def timelines(request):
    
    action = request.GET.get('search')
    
    if not action:
        return init_view(request)
        
    elif action == 'Search':
        return plot_reports(request)
        
    else:
        #no idea
        return HttpResponseServerError("no action determined")   
    
def init_view(request):
    
    dir_list = get_directory_tree_list()
    
    return render(request, "reports/timelines.html",
                  context={'dirList': dir_list,
                           }
                  )       
    
def plot_reports(request):
    dir_list = get_directory_tree_list()
    
    filter = selection_to_filter(request.GET.get('selected_dir'))
    
    focalDonut = FocalLengthDonut(filter)
    
    mobileVsCam = MobileVsCam(filter)
    
    mobileVsCamRat = MobileVsCamRatio(filter)
    
    
    return render(request, "reports/timelines.html", 
                  context={
                      'FocalLengthDonut_div': focalDonut.plot(), 
                      'CamerasOverTime_div': mobileVsCam.plot(),
                      'MobileVsCamRatio_div': mobileVsCamRat.plot(),
                      'dirList': dir_list
                           }
                  )
    
