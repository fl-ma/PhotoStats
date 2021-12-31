import exifread, os
from photostats.config import read_config_var
from photostats.constants import PHOTO_FILETYPES

dir = read_config_var("dir_example")
print(dir)


for filename in os.listdir(dir):

    #construct path and filetype
    filepath = os.path.realpath(os.path.join(dir, filename))
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

    for tag in tags.keys():
        if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote', 'Thumbnail'):
            print ("Key: %s, value %s" % (tag, tags[tag]))