from django.contrib import admin
from .models import Image, Camera, Lens

# Register your models here.
admin.site.register(Image)
admin.site.register(Camera)
admin.site.register(Lens)