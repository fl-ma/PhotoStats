import exifread
from photostats.config import read_config_var

path_name = read_config_var("photo_example")


# Open image file for reading (binary mode)
f = open(path_name, 'rb')

# Return Exif tags
tags = exifread.process_file(f)

for tag in tags.keys():
    if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
        print ("Key: %s, value %s" % (tag, tags[tag]))