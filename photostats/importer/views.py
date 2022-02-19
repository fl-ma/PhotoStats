from django.shortcuts import render
from django.http import HttpResponse, HttpResponseServerError
from django.template import loader

from images.models import Image
from directories.models import Directory
from . import ImporterLogic


def index(request):
    # https://docs.djangoproject.com/en/4.0/intro/tutorial04/
    # return HttpResponse("Hello, world. You're at the importer action.")

    # image_list = Image.objects.all()
    template = loader.get_template('importer/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def action(request):

    # determine button clicked
    try:
        button = get_button(request)

    except ValueError as exc:
        return HttpResponseServerError(str(exc))

    # handle buttons
    if button == 'List':
        return action_list(request)

    elif button == 'Delete':
        return action_delete(request)

    elif button == 'Import':
        return action_import(request)

    else:
        if not button:
            button = '<empty>'

        text = "Button clicked is unknown: " + button
        return HttpResponseServerError(text)


def get_button(request):
    # determine button that was clicked
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

    try:
        path = ImporterLogic.validate_path(request.POST.get('Ipath'))

        dir = Directory.objects.get(path=path)

    except Exception as inst:
        text = str(inst)
        return HttpResponseServerError(text)

    else:

        image_list = dir.image_set.all()

        template = loader.get_template('images/image_list.html')
        context = {
            'image_list': image_list
        }
        return HttpResponse(template.render(context, request))


def action_import(request):

    if request.POST.get('recursion') == 'recursion':
        recursive_scan = True
    else:
        recursive_scan = False

    if request.POST.get('scan files') == 'Scan files':
        files_scan = True
    else:
        files_scan = False

    try:
        status_list = ImporterLogic.do_import(
            request.POST.get('Ipath'), recursive_scan, files_scan)

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
