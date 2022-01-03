from django.db import models
from datetime import datetime

class Image(models.Model):
    filename = models.CharField(max_length=200)
    path =  models.CharField(max_length=200)
    date_taken = models.DateTimeField(null=True)

    camera_make =   models.CharField(max_length=100, null=True)
    camera_model =  models.CharField(max_length=100, null=True)
    lens_model =    models.CharField(max_length=100, null=True)
    
    focal_length =  models.PositiveSmallIntegerField(null=True)
    exposure_time = models.FloatField(null=True)
    aperture =      models.FloatField(null=True)

    class Meta:
        ordering = ["-filename"]

    def __str__(self):
        return (self.path + self.filename)


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
    
    #conversion to ensure format is correct
    datetime.strptime(out, '%Y-%m-%d %H:%M%S:%f')
    
    return out