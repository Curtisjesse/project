from django.db import models

# Create your models here.

class Doctors(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    specialized = models.TextField()
    img = models.ImageField(upload_to = 'images')
    
    def __str__(self):
        return self.name
    