import os.path 
import exifread, os
from photostats.constants import PHOTO_FILETYPES
import images.models
from images.models import Image

def validate_path(mypath):
    
    if not mypath:
        raise OSError('No path provided')
    
    if not os.path.isdir(mypath):
        raise OSError(str("path: " + mypath + " is invalid"))

def do_import(path):
    
    validate_path(path) 
    images = []

    for filename in os.listdir(path):

        #construct path and filetype
        filepath = os.path.realpath(os.path.join(path, filename))
        name, extension = os.path.splitext(filepath)

        #filter for photo files only (exclude .dlls, .txts, etc)
        if extension not in PHOTO_FILETYPES:
            continue

        # Open image file for reading (binary mode)
        f = open(filepath, 'rb')

        # Read Exif tags
        tags = exifread.process_file(f)

        #close file
        f.close()


        #map exif tags to model        
        img = Image()
        
        img.filename = filename
        img.path = path
        img.date_taken = tags.get('date_taken')
        
        img.camera_make =   tags.get('Image Make')
        img.camera_model =  tags.get('Image Model')
        img.lens_model =    tags.get('LensModel')     
        
        images.append(img)
        
        
    return images

