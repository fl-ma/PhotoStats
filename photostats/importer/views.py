from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    # https://docs.djangoproject.com/en/4.0/intro/tutorial04/
    # return HttpResponse("Hello, world. You're at the importer action.")

    # image_list = Image.objects.all()

    print("Index")

    template = loader.get_template('importer/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def action(request):
    print("action")
    return HttpResponse("Congrats, you clicked")