from django.db import models
from accounts.models import Doctor, Patient


# Create your models here.


    
    
class Doctors(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    specialized = models.TextField()
    img = models.ImageField(upload_to = 'images')
    # Socialmedia = models.ForeignKey(Socialmedia,related_name='socialmedia',on_delete=models.SET_NULL,null=True,blank=True)
    
    
    def __str__(self):
        return self.name

class Booking_Detail(models.Model):
    doctor = models.ForeignKey(Doctor, related_name='Doctor', on_delete=models.SET_NULL, null=True, blank=True)
    patient = models.ForeignKey(Patient, related_name='Patient', on_delete=models.CASCADE)
    booked_on = models.DateTimeField()
    date_booked = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.doctor.user.username} with {self.patient.user.username}"

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
class Medicine(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    img = models.ImageField(upload_to = 'images')
    
    
    def __str__(self):
        return self.title
    
class Testimonials(models.Model):
        name = models.CharField(max_length=100)
        description = models.TextField(max_length=1000, blank=False)
        img = models.ImageField(upload_to='Testimonials')
        
        def __str__(self):
            return self.name
        

class Contact_info(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    
    def __str__(self):
        return self.name       
        