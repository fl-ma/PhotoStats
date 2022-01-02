import os.path 
import errno
import exifread, os
from photostats.constants import PHOTO_FILETYPES
import images.models
from images.models import Image, format_datetime, fraction_to_float


def createImage(path, filename):
    
    #construct path and filetype
    filepath = os.path.realpath(os.path.join(path, filename))
    name, extension = os.path.splitext(filepath)

    #filter for photo files only (exclude .dlls, .txts, etc)
    if extension not in PHOTO_FILETYPES:
        raise OSError(errno.EIO, "Filetype not supported", filename)
       
    # Open image file for reading (binary mode)
    f = open(filepath, 'rb')

    # Read Exif tags 
    # (speed up processing by ignoring thumbnail and makernotes)
    tags = exifread.process_file(f, details=False)

    #close file
    f.close()
 
    #map exif tags to data model
    img = Image()
        
    img.filename = filename
    img.path = path
    img.date_taken = format_datetime(tags.get('EXIF DateTimeOriginal'))
        
    img.camera_make     = tags.get('Image Make')
    img.camera_model    = tags.get('Image Model')
    img.lens_model      = tags.get('EXIF LensModel')     
        
    img.focal_length        = fraction_to_float(tags.get('EXIF FocalLength'))
    img.exposure_time       = fraction_to_float(tags.get('EXIF ExposureTime'))
    img.aperture            = fraction_to_float(tags.get('EXIF FNumber'))
    # print(img.filename, tags.get('EXIF FocalLength'), tags.get('EXIF ExposureTime'), tags.get('EXIF FNumber'))
    
    return img