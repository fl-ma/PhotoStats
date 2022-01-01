from django.db import models

# Create your models here.

class Image(models.Model):
    filename = models.CharField(max_length=200)
    path =  models.CharField(max_length=200)
    date_taken = models.DateTimeField()

    camera_make =   models.CharField(max_length=100)
    camera_model =  models.CharField(max_length=100)
    lens_model =    models.CharField(max_length=100, null=True)
    
    # https://docs.djangoproject.com/en/4.0/intro/tutorial02/

# Key: GPS GPSVersionID, value [2, 2, 0, 0]
# Key: GPS GPSLatitudeRef, value S
# Key: GPS GPSLatitude, value [41, 16, 3099/625]
# Key: GPS GPSLongitudeRef, value E
# Key: GPS GPSLongitude, value [173, 47, 1181/619]
# Key: GPS GPSAltitudeRef, value 0
# Key: GPS GPSAltitude, value 128492/957
# Key: GPS GPSTimeStamp, value [0, 5, 44]
# Key: GPS GPSSpeedRef, value K
# Key: GPS GPSSpeed, value 6574/1255
# Key: GPS GPSMapDatum, value WGS-84
# Key: GPS GPSDate, value 2019:03:28

# Key: Image Make, value Canon
# Key: Image Model, value Canon EOS 750D
# EXIF LensModel, value EF-S10-18mm f/4.5-5.6 IS STM

# Key: EXIF ExposureTime, value 1/400
# Key: EXIF FNumber, value 11


def format_datetime(input):
    # 2017:07:04 19:07:42
    # It must be in YYYY-MM-DD HH:MM[:ss
    date = str(input).strip()
    date = str(date[:10])
    elements = date.split(":")
    date = '-'.join(elements)
    
    time = str(input).strip()
    time = time[11:]
    
    out = str(date + " " + time )
    
    return out