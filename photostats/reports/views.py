from django.shortcuts import render
from django.http import HttpResponse, HttpResponseServerError
from django.template import loader

from plotly.offline import plot

from images.models import Image

from .repFocalLengthDonut import FocalLengthDonut
from .repMobileVsCam import MobileVsCam

def index(request):
    image_list = Image.objects.filter(camera_make='Canon')
    
    chart = FocalLengthDonut(image_list)
    plt_div = plot(chart.fig, output_type='div')
    
    chart2 = MobileVsCam()
    plt2_div = plot(chart2.fig, output_type='div')
    
    
    return render(request, "reports/index.html", 
                  context={'FocalLengthDonut_div': plt_div, 
                           'CamerasOverTime_div': plt2_div})
    
    # template = loader.get_template('importer/index.html')
    # context = {}
    # return HttpResponse(template.render(context, request))