import os.path 
import errno
import exifread, os
from fractions import Fraction

from photostats.constants import PHOTO_FILETYPES
from images.models import Image, format_datetime, fraction_to_float


def createImage(filepath):
    
    name, extension = os.path.splitext(filepath)

    #filter for photo files only (exclude .dlls, .txts, etc)
    if extension not in PHOTO_FILETYPES:
        raise OSError(errno.EIO, "Filetype not supported", name)
       
    # Open image file for reading (binary mode)
    f = open(filepath, 'rb')

    # Read Exif tags 
    # (speed up processing by ignoring thumbnail and makernotes)
    tags = exifread.process_file(f, details=False)

    #close file
    f.close()
 
    #map exif tags to data model
    img = Image()
    
    img.path, img.filename = os.path.split(filepath)
    img.date_taken = format_datetime(tags.get('EXIF DateTimeOriginal'))
        
    img.camera_make     = tags.get('Image Make')
    img.camera_model    = tags.get('Image Model')
    img.lens_model      = tags.get('EXIF LensModel')     
        
    img.focal_length        = fraction_to_float(tags.get('EXIF FocalLength'))
    img.exposure_time       = fraction_to_float(tags.get('EXIF ExposureTime'))
    img.aperture            = fraction_to_float(tags.get('EXIF FNumber'))
    
    img.exposure_time_str   = tags.get('EXIF ExposureTime').printable   
    img.aperture_str        = tags.get('EXIF FNumber').printable
    
    return img