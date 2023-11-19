from django.db import models

# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=202)
    body = models.TextField()

    create_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title