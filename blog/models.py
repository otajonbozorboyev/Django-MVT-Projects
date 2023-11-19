from django.db import models

# Create your models here.

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
    body_one = models.TextField()
    image = models.ImageField(upload_to='blog/')
    body_two = models.TextField()
    tag = models.ManyToManyField(Tag, )

    update_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
        blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='Comment')
        full_name = models.CharField(max_length=202)
        email = models.EmailField()
        phone = models.CharField(max_length=202)
        message = models.TextField()

        create_date = models.DateTimeField(auto_now_add=True)
        updated_date = models.DateTimeField(auto_now=True)

        def __str__(self) -> str:
            return self.full_name
        

class Subscribe(models.Model):
    email = models.EmailField()

    is_published = models.BooleanField(default=False)
    update_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
