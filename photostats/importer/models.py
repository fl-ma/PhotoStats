from django.db import models

# Create your models here.
class Importer(models.Model):
    import_path = models.CharField(max_length=200)