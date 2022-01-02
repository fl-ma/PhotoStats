import os.path 
from images.imageFactory import createImage

def validate_path(mypath):
    
    if not mypath:
        raise OSError('No path provided')
    
    if not os.path.isdir(mypath):
        raise OSError(str("path: " + mypath + " is invalid"))

def do_import(path):
    
    validate_path(path) 
    images = []

    for filename in os.listdir(path):
        try:
            img = createImage(path, filename)
            
        except OSError as inst:
            #filetype does not match (e.g. txt, dll)
            continue

        
        img.save()
        
        images.append(img)
        
    return images