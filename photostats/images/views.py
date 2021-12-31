from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Image

# Create your views here.
def list(request):
    image_list = Image.objects.all()

    template = loader.get_template('images/index.html')
    context = {
        'image_list': image_list,
    }
    return HttpResponse(template.render(context, request))