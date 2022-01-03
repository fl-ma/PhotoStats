import os.path 
from images.imageFactory import createImage
import logging

from images.imageError import ExifError

def validate_path(mypath):
    
    logger = logging.getLogger()
    
    if not mypath:
        msg = 'No path provided'
        logger.critical(msg)
        raise OSError(msg)
    
    if not os.path.isdir(mypath):
        msg = str("path: " + mypath + " is invalid")
        logger.critical(msg)
        raise OSError(msg)

def do_import(path, subdir=False, update=False):
    '''
        path    = directory to scan
        subdir  = also scan files in sub directories (recursive)
        update  =   true    -> query database and update existing files
                    false   -> crate without query (might result in duplicates)
    '''
    
    validate_path(path) 
    images = []
    
    logger = logging.getLogger()
    

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
            
            if not os.path.isdir(filepath):
                logger.warning(filepath + " skipped due to filetype")
            continue
        
        except ExifError as exc:
            logger.error(exc.message + 'skipping import')
            continue
    
        images.append(img) 
        
    return images