from PIL import Image, ExifTags
from PIL.ExifTags import TAGS

from images.imageError import ExifError

def read(path):
    '''
        read exif tags and map them to human-readable format
    '''
    img = Image.open(path)
    
    exif = img._getexif()
    
    if not exif:
        raise ExifError(path, "No exif tags found")
    
    labeled = {}
    for (key, val) in exif.items():
        labeled[TAGS.get(key)] = val      
        
    img.close()
    
    return labeled