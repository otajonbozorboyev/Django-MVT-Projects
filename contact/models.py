from django.db import models

# Create your models here.

class Contact(models.Model):
    full_name = models.CharField(max_length=202)
    email = models.EmailField()
    phone = models.CharField(max_length=202)
    message = models.TextField()

    is_published = models.BooleanField(default=False)
    update_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class ContactMe(models.Model):
    address = models.CharField(max_length=202)
    phone = models.CharField(max_length=202)
    email = models.EmailField()
    website = models.CharField(max_length=202)

    def __str__(self):
        return self.phone