import os.path 
import errno
import os
from fractions import Fraction

from photostats.constants import PHOTO_FILETYPES
from images.models import Image, format_datetime, fraction_to_float
from images.imageError import ExifError
from images.imageExif import read


def createImage(filepath, update=False):
    '''
        update  =   true    -> query database and update existing files
                    false   -> crate without query (might result in duplicates)
    '''    
    name, extension = os.path.splitext(filepath)
    path, filename  = os.path.split(filepath)

    #filter for photo files only (exclude .dlls, .txts, etc)
    if extension not in PHOTO_FILETYPES:
        raise OSError(errno.EIO, "Filetype not supported", name)
       
    # Read Exif tags 
    tags = read(filepath)
    
    if not tags:
        raise ExifError(filepath, "No exif tags found")
     
    if update:
        try:
            img = Image.objects.get(path=path, filename=filename)
        except:
            img = Image()
    
    else:
        img = Image()
    
    #map exif tags to data model
    img.path       = path
    img.filename   = filename
    img.date_taken = format_datetime(tags.get('DateTimeOriginal'))
        
    img.camera_make     = tags.get('Make')
    img.camera_model    = tags.get('Model')
    img.lens_model      = tags.get('LensModel')     
        
    img.focal_length    = tags.get('FocalLength')
    img.exposure_time   = tags.get('ExposureTime')
    img.aperture        = tags.get('FNumber')
    
    return img