from django.shortcuts import render
from django.http import HttpResponse, HttpResponseServerError
from django.template import loader

from images.models import Image
from . import ImporterLogic

def index(request):
    # https://docs.djangoproject.com/en/4.0/intro/tutorial04/
    # return HttpResponse("Hello, world. You're at the importer action.")

    # image_list = Image.objects.all()
    template = loader.get_template('importer/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def action(request):
    
    #determine button clicked
    try:
        button = get_button(request)
        
    except ValueError as exc:
        return HttpResponseServerError(str(exc))

    #handle buttons        
    if button == 'List':
        return action_list(request)
        
    elif button == 'Delete':
        return action_delete(request)
        
    elif button =='Import':
        return action_import(request)
        
    else:
        if not button:
            button = '<empty>'
        
        text = "Button clicked is unknown: " + button
        return HttpResponseServerError(text)


def get_button(request):
    #determine button that was clicked
    button = request.POST.get('list')
    
    if not button:
        button = request.POST.get('delete')
        
    if not button:
        button = request.POST.get('import')
        
    if not button:
        text = 'No button found'
        raise ValueError(text)
        
    return button
        

def action_list(request):  
    
    path = request.POST.get('Ipath')
    
    if path:
        image_list = Image.objects.filter(path=path)
        
    else:
        image_list = Image.objects.all()
        
    template = loader.get_template('images/image_list.html')
    context = {
        'image_list' : image_list
    }
    return HttpResponse(template.render(context, request))


def action_import(request):
    
    if request.POST.get('recursion') == 'recursion':
        recursive_scan = True
    else:
        recursive_scan = False
        
    if request.POST.get('radio_upd') == 'Update':
        update = True
    else:
        update = False
    
    try:
        status_list = ImporterLogic.do_import(request.POST.get('Ipath'), recursive_scan, update)
        
    except Exception as inst:
        text = str(inst)
        return HttpResponseServerError(text)
    
    else:         
        template = loader.get_template('importer/import_status.html')
        context = {
            'import_list': status_list
        }
        return HttpResponse(template.render(context, request))
    
def action_delete(request):

    try:
        message = ImporterLogic.delete(request.POST.get('Ipath'))
        
    except Exception as inst:
        text = str(inst)
        return HttpResponseServerError(text)
    
    else:         
        return HttpResponse(message)
    