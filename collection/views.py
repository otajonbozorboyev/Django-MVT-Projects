from django.shortcuts import render
from about.models import About
from blog.models import Blog, Category
from contact.models import ContactMe
from .models import Collection

def collectionView(request):
    category = Category.objects.all()
    contactme = ContactMe.objects.all()
    blog = Blog.objects.all().order_by('-id')
    about = About.objects.all()
    collection = Collection.objects.all().order_by('-id')[:5]
    context = {
        'abouts': about,
        'cme': contactme,
        'categories': category,
        'blogs': blog,
        'collections': collection
    }
    return render(request, 'collection.html', context)