import os.path 
import errno
import os
import logging

from photostats.constants import PHOTO_FILETYPES, IMPORT_LOG_NAME
from images.models import Image, Camera, Lens, format_datetime
from images.imageError import ExifError
from images.imageExif import read


def createImage(filepath, update=False):
    '''
        update  =   true    -> query database and update existing files
                    false   -> crate without query (might result in duplicates)
    '''    
    name, extension = os.path.splitext(filepath)
    path, filename  = os.path.split(filepath)
    
    logger = logging.getLogger(IMPORT_LOG_NAME)

    #filter for photo files only (exclude .dlls, .txts, etc)
    if extension not in PHOTO_FILETYPES:
        raise OSError(errno.EIO, "Filetype not supported", name)
    
    logger.info(filepath + ":")
       
    # Read Exif tags 
    tags = read(filepath)
    
    if not tags:
        raise ExifError(filepath, "No exif tags found")
     
    if update:
        try:
            img = Image.objects.get(path=path, filename=filename)
            logger.info("IMG already in database - update")
            
        except:
            img = Image()
            logger.info("IMG not found in database - insert")
    
    else:
        img = Image()
    
    #map exif tags to data model
    img.path       = path
    img.filename   = filename
    
    img.date_taken = handle_date_taken(tags, filepath)        
        
    img.focal_length    = tags.get('FocalLength')
    img.exposure_time   = tags.get('ExposureTime')
    img.aperture        = tags.get('FNumber')
     
    
    cam, created = Camera.objects.get_or_create(
        camera_make=tags.get('Make'), 
        camera_model=tags.get('Model'))
    
    img.camera = cam
    
    tag_lens = tags.get('LensModel')
    
    if tag_lens:    
        lens, created = Lens.objects.get_or_create(
            lens_model = tag_lens)
        
        img.lens = lens
    
    return img


def handle_date_taken(tags, filepath):
    
    try:
        date_taken = format_datetime(tags.get('DateTimeOriginal'))
    except:
        #fallback to other date field
        date_taken = format_datetime(tags.get('DateTime'))
    
    #still nothing? can't use
    if date_taken is None:
        raise ExifError(filepath, "No datetime found or not convertible")
    
    return date_taken