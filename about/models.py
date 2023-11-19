from django.db import models

# Create your models here.

class About(models.Model):
    full_name = models.CharField(max_length=202)
    title = models.CharField(max_length=202)
    image = models.ImageField(upload_to='about/')
    description = models.TextField()
    linkedin = models.CharField(max_length=202)
    instagram = models.CharField(max_length=202)
    github = models.CharField(max_length=202)
    telegram = models.CharField(max_length=202)

    create_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
    
class Section(models.Model):
    title = models.CharField(max_length=202)
    numbers = models.IntegerField()

    def __str__(self):
        return self.title
    

