from django.shortcuts import render
from django.http import HttpResponse, HttpResponseServerError
from django.template import loader
from images.models import Image
from plotly.offline import plot
from .repFocalLengthDonut import FocalLengthDonut

def index(request):
    image_list = Image.objects.filter(camera_make='Canon')
    
    chart = FocalLengthDonut(image_list)
    plt_div = plot(chart.fig, output_type='div')
    
    
    return render(request, "reports/index.html", context={'plot_div': plt_div})
    
    # template = loader.get_template('importer/index.html')
    # context = {}
    # return HttpResponse(template.render(context, request))