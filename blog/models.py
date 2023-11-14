from django.db import models

# Create your models here.

class About(models.Model):
    name = models.CharField(max_length=202)
    image = models.ImageField()
    body = models.TextField()

    linkedin = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    GitHub = models.URLField(blank=True, null=True)
    telegram = models.URLField(blank=True, null=True)



    def __str__(self):
        return self.name
    

class Category(models.Model):
    title = models.CharField(max_length=202)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=202)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=202)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    image = models.ImageField(upload_to='blog/')
    body = models.TextField()
    tag = models.ManyToManyField(Tag, )

    upload_date = models.DateField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    full_name = models.CharField(max_length=202)
    email = models.EmailField()
    phone = models.CharField(max_length=202)
    message = models.TextField()

    upload_date = models.DateField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class Skill(models.Model):
    title = models.CharField(max_length=202)
    degree = models.IntegerField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    full_name = models.CharField(max_length=202)
    email = models.EmailField()
    phone = models.CharField(max_length=202)
    message = models.TextField()


    upload_date = models.DateField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.full_name



class Subscribe(models.Model):
    email = models.EmailField()


    def __init__(self):
        return self.email