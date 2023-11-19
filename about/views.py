from django.shortcuts import render
from blog.models import Blog, Category
from contact.models import ContactMe
from .models import About, Section
from collection.models import Collection


def aboutView(request):
    about = About.objects.all()
    section = Section.objects.all()
    contactme = ContactMe.objects.all()
    collection = Collection.objects.all().order_by('-id')[:5]
    category = Category.objects.all()
    blog = Blog.objects.all().order_by('-id')
    context = {
        'abouts': about,
        'cme': contactme,
        'collections': collection,
        'categories': category,
        'blogs': blog,
        'sections':section
    }
    return render(request, 'about.html', context)

