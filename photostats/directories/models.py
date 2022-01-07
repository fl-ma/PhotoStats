from django.db import models

class Directory(models.Model):
    
    path = models.CharField(max_length=200, unique=True)
    text = models.CharField(max_length=200, null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    selectable = models.BooleanField(default=False)

    def __str__(self):
        if self.text:
            return self.text
        
        else:
            return self.path
    
    #fix the fact that djando admin does not allow saving empty strings even though 
    #the field is null-able
    def save(self, *args, **kwargs):
        if not self.parent:
            self.parent = None
              
        if not self.text:
            self.text = None
        super(Directory, self).save(*args, **kwargs)