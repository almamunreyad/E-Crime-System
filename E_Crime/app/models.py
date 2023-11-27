from django.db import models

# Create your models here.

class Form(models.Model):
    image = models.ImageField(upload_to='media/')
    crim_id = models.CharField(max_length=10000)
    name = models.CharField(max_length=200)
    nation_id = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    gender = models.CharField(max_length=1)
    date = models.DateField()
    report = models.TextField()
    
class Criminal_List(models.Model):
    criminal_id = models.CharField(max_length=10000)
    criminal_name =  models.CharField(max_length=200)
    crime_type = models.TextField()
    criminal_image = models.ImageField(upload_to='media/criminal')
    
class SignUp(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=20)