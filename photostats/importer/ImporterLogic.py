import os.path 
from images.imageFactory import createImage

def validate_path(mypath):
    
    if not mypath:
        raise OSError('No path provided')
    
    if not os.path.isdir(mypath):
        raise OSError(str("path: " + mypath + " is invalid"))

def do_import(path, recursive=False):
    
    validate_path(path) 
    images = []

    for filename in os.listdir(path):
        
        filepath = os.path.realpath(os.path.join(path, filename))
        
        if recursive and os.path.isdir(filepath):
            sub_imgs = do_import(filepath, True)
            
            for img in sub_imgs:
                images.append(img)
        
        try:
            img = createImage(filepath)
            
        except OSError as inst:
            #filetype does not match (e.g. txt, dll)
            continue
    
        images.append(img) 
        
    return images