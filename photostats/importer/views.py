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
        return HttpResponseServerError('List - not yet implemented')
        
    elif button == 'Delete':
        return HttpResponseServerError('Delete - not yet implemented')
        
    elif button =='Import':
        
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
            # return HttpResponse( str(len(images)) + " images successfully imported!")            
            template = loader.get_template('importer/import_status.html')
            context = {
                'import_list': status_list
            }
            return HttpResponse(template.render(context, request))
        
    else:
            text = "Button clicked is unknown: " + button
            return HttpResponseServerError(text)
        
