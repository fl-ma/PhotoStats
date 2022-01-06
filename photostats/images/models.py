from django.db import models
from datetime import datetime
import os

class Camera(models.Model):
    camera_make =   models.CharField(max_length=100, null=True)
    camera_model =  models.CharField(max_length=100, null=True)
    
    class Meta:
        unique_together = ['camera_make', 'camera_model']
    
    def __str__(self):
        
        if self.camera_make:
            make = self.camera_make
        else:
            make = '<unknown>'

        if self.camera_model:
            model = self.camera_model
        else:
            model = '<unknown>'            
        
        return (make + ': ' + model)
            
class Lens(models.Model):
    lens_model =    models.CharField(max_length=100, blank=True)    
    
    #does not work due to empty string
    # def __str__(self):
    #     return (self.lens_model)

class Image(models.Model):
    filename = models.CharField(max_length=200)
    path =  models.CharField(max_length=200)
    date_taken = models.DateTimeField(null=True)
    
    camera = models.ForeignKey(Camera, on_delete=models.SET_NULL, null=True)
    lens = models.ForeignKey(Lens, on_delete=models.SET_NULL, null=True)
    
    focal_length =  models.PositiveSmallIntegerField(null=True)
    exposure_time = models.FloatField(null=True)
    aperture =      models.FloatField(null=True)

    class Meta:
        ordering = ["-filename"]
        unique_together = ['filename', 'path']

    def __str__(self):
        return (os.path.join(self.path, self.filename))


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