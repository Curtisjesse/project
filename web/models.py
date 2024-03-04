from django.db import models

# Create your models here.

class Socialmedia(models.Model):
    facebook_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    
    
class Doctors(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    specialized = models.TextField()
    img = models.ImageField(upload_to = 'images')
    Socialmedia = models.ForeignKey(Socialmedia,related_name='socialmedia',on_delete=models.SET_NULL,null=True,blank=True)
    
    
    def __str__(self):
        return self.name
    
class Departments(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    img = models.ImageField(upload_to = 'images')
    
    
    def __str__(self):
        return self.title
class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    img = models.ImageField(upload_to = 'images')
    
    
    def __str__(self):
        return self.title