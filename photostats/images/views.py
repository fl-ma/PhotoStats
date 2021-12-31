from django.shortcuts import render
from django.http import HttpResponse
from .models import Image

# Create your views here.
def list(request):
    image_list = Image.objects.all()
    output = ', '.join([i.filename for i in image_list])
    return HttpResponse(output)