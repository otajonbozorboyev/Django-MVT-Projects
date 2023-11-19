from django.shortcuts import render
from blog.models import Blog, Category
from .models import Service
from about.models import About
from contact.models import ContactMe 
from collection.models import Collection

# Create your views here.

def serviceView(request):
    service = Service.objects.all()
    collection = Collection.objects.all()
    contactme = ContactMe.objects.all()
    about = About.objects.all()
    category = Category.objects.all()
    blog = Blog.objects.all().order_by('-id')
    context = {
        'abouts': about,
        'collections': collection,
        'cme': contactme,
        'categories': category,
        'blogs': blog,
        'service': service
    }
    return render(request, 'services.html', context)