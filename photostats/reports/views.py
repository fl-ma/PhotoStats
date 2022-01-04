from django.shortcuts import render

from .repFocalLengthDonut import FocalLengthDonut
from .repMobileVsCam import MobileVsCam

def index(request):
    
    
    focalDonut = FocalLengthDonut('Focal Lengths')
    
    mobileVsCam = MobileVsCam('Mobile vs. Camera')
    
    
    return render(request, "reports/index.html", 
                  context={'FocalLengthDonut_div': focalDonut.plot(), 
                            'CamerasOverTime_div': mobileVsCam.plot(),
                           }
                  )
    
    # template = loader.get_template('importer/index.html')
    # context = {}
    # return HttpResponse(template.render(context, request))