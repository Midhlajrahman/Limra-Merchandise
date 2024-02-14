from django.db import models

# Create your models here.


class BusinessLines(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='businesslines/')
    description = models.TextField()
    
    def __str__(self):
        return self.title
    
    
class Team(models.Model):
    name = models.CharField(max_length = 200)
    position =  models.CharField(max_length = 200)
    image = models.ImageField(upload_to="team/")
    
    def __str__(self):
        return self.name
    

class News(models.Model):
    title = models.CharField(max_length = 200)
    desciption = models.TextField()
    date = models.IntegerField()
    month = models.CharField(max_length = 200)
    image = models.ImageField(upload_to="news")
    
    def __str__(self):
        return self.title
    

class Contact(models.Model):
    name = models.CharField(max_length = 200)
    email = models.EmailField()
    number = models.IntegerField()
    subject = models.CharField(max_length = 250)
    message = models.TextField()
    
    def __str__(self):
        return self.name
    
    
class Enquiry(models.Model):
    name = models.CharField(max_length = 200)
    email = models.EmailField()
    subject = models.CharField(max_length = 250)
    message = models.TextField()
    
    def __str__(self):
        return self.name
    