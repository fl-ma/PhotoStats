from django.shortcuts import render
from django.http import HttpResponse, HttpResponseServerError
from django.template import loader
from . import ImporterLogic

def index(request):
    # https://docs.djangoproject.com/en/4.0/intro/tutorial04/
    # return HttpResponse("Hello, world. You're at the importer action.")

    # image_list = Image.objects.all()
    template = loader.get_template('importer/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def action(request):
    
    #determine button that was clicked
    button = request.POST.get('list')
    
    if not button:
        button = request.POST.get('delete')
        
    if not button:
        button = request.POST.get('import')
    
    #handle buttons        
    if button == 'List':
        print(button)
        
    elif button == 'Delete':
        print(button)
        
    elif button =='Import':
        try:
            ImporterLogic.do_import(request.POST.get('Ipath'))
            
        except Exception as inst:
            text = str(inst)
            return HttpResponseServerError(text)
        
        else:
            return HttpResponse("Worked!")
        
    else:
            text = "Button clicked is unknown: " + button
            return HttpResponseServerError(text)
        
