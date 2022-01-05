import os.path 
from images.imageFactory import createImage
import logging
from datetime import datetime

from images.imageError import ExifError
from photostats.constants import IMPORT_LOG_NAME
from images.models import Image

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
    
    #libraries can handle with and without closing \
    #however on the database it makes a difference
    if mypath[-1:] == '\\':
        return mypath
    
    else:
        return mypath + '\\'
        

def do_import(path, subdir=False, update=False):
    '''
        path    = directory to scan
        subdir  = also scan files in sub directories (recursive)
        update  =   true    -> query database and update existing files
                    false   -> crate without query (might result in duplicates)
    '''
    
    #initialize logger and clear log file before start
    logger = logging.getLogger(IMPORT_LOG_NAME)
    
    logfile = logger.handlers[0].baseFilename
    with open(logfile, 'w'):
        pass
    
    logger.info("Import started: " + str(datetime.now()) + " on folder " + path)
    
    #the above is separated from the actual import below to keep the init-stuff out 
    #of the recursion
    imgs = import_folder(path, logger, subdir, update)
    
    #at the very end: persists and return log     
    idx = 0
    for img in imgs:
        img.save()
        logger.info(img.path + img.filename + " saved")
        idx += 1
        
    logger.info(str(idx) + ' images saved')
    
    #retrieve logfile (so it can be displayed in UI)
    logfile = logger.handlers[0].baseFilename
    with open(logfile, 'r') as f:
        lines = f.read().splitlines()
    
    f.close()
    return lines

def import_folder(path, logger, subdir=False, update=False):
    
    mypath = validate_path(path) 
    images = []
    
    #handle first all images in the folder
    for filename in os.listdir(mypath):
        
        filepath = os.path.realpath(os.path.join(mypath, filename))
        
        if os.path.isdir(filepath):
            #ignore directories here
            continue
        
        try:
            img = createImage(filepath, update)
            
        except OSError as inst:            
            msg = filepath + " skipped due to filetype"
            logger.warning(msg)
            continue
        
        except ExifError as exc:
            msg = exc.filename + ': ' + exc.message + ': skipping import'
            logger.error(msg)
            continue
    
        images.append(img)
        
    #then handle all subfolders (if required)
    if subdir:
    
        for dir in os.listdir(mypath):
            subdirpath = os.path.realpath(os.path.join(mypath, dir))
            
            if not os.path.isdir(subdirpath):
                #ignore everything that is not a directory
                continue
            
            sub_imgs = import_folder(subdirpath, logger, subdir, update)
            
            images.extend(sub_imgs)   
        
    return images

        
def delete(path):
    
    mypath = validate_path(path)
    
    list = Image.objects.filter(path=mypath)
    
    message = str(len(list)) + ' images deleted from path ' + mypath
    
    list.delete()
    
    return message