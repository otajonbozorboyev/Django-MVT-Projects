from django.db import models

# Create your models here.

class Collection(models.Model):
    title = models.CharField(max_length=202)
    image  = models.ImageField(upload_to='collection/')

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title