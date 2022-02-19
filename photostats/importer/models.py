from django.db import models


class Importer(models.Model):
    import_path = models.CharField(max_length=200)
