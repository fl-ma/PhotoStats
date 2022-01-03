import os.path 
from images.imageFactory import createImage

def validate_path(mypath):
    
    if not mypath:
        raise OSError('No path provided')
    
    if not os.path.isdir(mypath):
        raise OSError(str("path: " + mypath + " is invalid"))

def do_import(path, subdir=False, update=False):
    '''
        path    = directory to scan
        subdir  = also scan files in sub directories (recursive)
        update  =   true    -> query database and update existing files
                    false   -> crate without query (might result in duplicates)
    '''
    
    validate_path(path) 
    images = []

    for filename in os.listdir(path):
        
        filepath = os.path.realpath(os.path.join(path, filename))
        
        if subdir and os.path.isdir(filepath):
            sub_imgs = do_import(filepath, True)
            
            for img in sub_imgs:
                images.append(img)
        
        try:
            img = createImage(filepath, update)
            
        except OSError as inst:
            #filetype does not match (e.g. txt, dll)
            continue
    
        images.append(img) 
        
    return images