import os.path 
from images.imageFactory import createImage
import logging
from datetime import datetime

from images.imageError import ExifError
from photostats.constants import IMPORT_LOG_NAME

def validate_path(mypath):
    
    logger = logging.getLogger(IMPORT_LOG_NAME)
    
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
    logger = logging.getLogger(IMPORT_LOG_NAME)
    logger.info("Import started: " + str(datetime.now()) + " on folder " + path)
    
    validate_path(path) 
    images = []

    
    #handle first all images in the folder
    for filename in os.listdir(path):
        
        filepath = os.path.realpath(os.path.join(path, filename))
        
        if os.path.isdir(filepath):
            #ignore directories here
            continue
        
        try:
            img = createImage(filepath, update)
            
        except OSError as inst:            
            logger.warning(filepath + " skipped due to filetype")
            continue
        
        except ExifError as exc:
            logger.error(exc.filename + ': ' + exc.message + ': skipping import')
            continue
    
        images.append(img)
        
    #then handle all subfolders (if required)
    if subdir:
    
        for dir in os.listdir(path):
            dirpath = os.path.realpath(os.path.join(path, dir))
            
            if not os.path.isdir(dirpath):
                #ignore everything that is not a directory
                continue
            
            sub_imgs = do_import(dirpath, True)
            
            images.extend(sub_imgs)   
        
    return images