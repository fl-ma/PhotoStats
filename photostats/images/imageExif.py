from PIL import Image, ExifTags
from PIL.ExifTags import TAGS

def read(path):

    img = Image.open(path)
    
    exif = img._getexif()
    
    labeled = {}
    for (key, val) in exif.items():
        labeled[TAGS.get(key)] = val    
    
    # for (key, val) in labeled.items():
    #     print(f"{key:25}: {val}")        
        
    img.close()
    
    return labeled