import os.path 
from images.imageFactory import createImage
import logging
from datetime import datetime

from images.imageError import ExifError, ImageError
from photostats.constants import IMPORT_LOG_NAME
from images.models import Image
from directories.models import Directory

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
    
    #python os libraries treat paths with or without trailing \ equally
    #since we save the path to UI it should be unique
    #removing trailing \ since this is the same as os.path.split() returns
    if mypath[-1:] == '\\':
        return mypath[:-1]
    
    else:
        return mypath
        

def do_import(path, subdir=False, files_scan=False):
    '''
        path    = directory to scan
        subdir  = also scan files in sub directories (recursive)
    '''
    
    #initialize logger and clear log file before start
    logger = logging.getLogger(IMPORT_LOG_NAME)
    
    logfile = logger.handlers[0].baseFilename
    with open(logfile, 'w'):
        pass
    
    logger.info("Import started: " + str(datetime.now()) + " on folder " + path)
    
    #the above is separated from the actual import below to keep the init-stuff out 
    #of the recursion
    imgs = import_folder(path, None, logger, subdir, files_scan)
    
    #save all images at the end
    for img in imgs:
        img.save()
        
    logger.info(str(len(imgs)) + ' images saved')
    
    #retrieve logfile (so it can be displayed in UI)
    logfile = logger.handlers[0].baseFilename
    with open(logfile, 'r') as f:
        lines = f.read().splitlines()
    
    f.close()
    return lines

def import_folder(path, parent, logger, subdir=False, files_scan=False):
    
    myDir, created = Directory.objects.get_or_create(path=validate_path(path))
    
    if parent:
        myDir.parent = parent
        
    if created:
        #save so we can access in the next step
        myDir.save()
    
    images = []
    
    #handle first all images in the folder
    if files_scan:
        for filename in os.listdir(myDir.path):
            
            filepath = os.path.realpath(os.path.join(myDir.path, filename))
            
            if os.path.isdir(filepath):
                #ignore directories here
                continue
            
            try:
                img = createImage(filename, myDir)
            
            except ExifError as exc:
                msg = exc.filename + ': ' + exc.message + ': skipping import'
                logger.error(msg)
                continue
            
            except ImageError as inst:            
                msg = filepath + " skipped due to filetype"
                logger.warning(msg)
                continue
            images.append(img)
        
    #then handle all subfolders (if required)
    if subdir:
    
        for dir in os.listdir(path):
            subdirpath = os.path.realpath(os.path.join(myDir.path, dir))
            
            if not os.path.isdir(subdirpath):
                #ignore everything that is not a directory
                continue
            
            sub_imgs = import_folder(subdirpath, myDir, logger, subdir, files_scan)
            
            images.extend(sub_imgs)   
        
    return images

        
def delete(path):
    
    mypath = validate_path(path)
    
    list = Image.objects.filter(path=mypath)
    
    message = str(len(list)) + ' images deleted from path ' + mypath
    
    list.delete()
    
    return message