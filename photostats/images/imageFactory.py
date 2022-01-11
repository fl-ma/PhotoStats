import os.path 
import os
import logging

from photostats.constants import PHOTO_FILETYPES, IMPORT_LOG_NAME
from images.models import Image, Camera, Lens, format_datetime
from images.imageError import ExifError, ImageError
from images.imageExif import read


def createImage(filename, directory):
    '''
        Create image dataset in database and add information from exif
    '''    
   
    logger = logging.getLogger(IMPORT_LOG_NAME)
    
    img, existed = Image.objects.get_or_create(filename=filename, path=directory)
    logger.info('Processing: ' + str(img) + ":")

    # filter for photo files only (exclude .dlls, .txts, etc)
    if img.get_file_type() not in PHOTO_FILETYPES:
        raise ImageError("Filetype not supported", str(img))
       
    # Read Exif tags 
    tags = read(str(img.get_path()))
    
    if not tags:
        raise ExifError(directory.path, "No exif tags found")    
    
    #map exif tags to data model
    img.date_taken = handle_date_taken(tags, directory.path)        
        
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
        try:
            date_taken = format_datetime(tags.get('DateTime'))
            
        except:
            date_taken = None
    
    #still nothing? can't use
    if date_taken is None:
        raise ExifError(filepath, "No datetime found or not convertible")
    
    return date_taken