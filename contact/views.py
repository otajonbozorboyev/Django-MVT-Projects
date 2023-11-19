from django.shortcuts import render, redirect
from blog.models import Blog, Category
from .forms import ContactForm
from .models import ContactMe
from about.models import About
from collection.models import Collection


def contactView(request):
    about = About.objects.all()
    collection = Collection.objects.all()
    contactme = ContactMe.objects.all()
    category = Category.objects.all()
    blog = Blog.objects.all().order_by('-id')
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('.')
    context = {
        'abouts': about,
        'collections': collection,
        'categories': category,
        'blogs': blog,
        'cme': contactme,
        'form': form
    }
    return render(request, 'contact.html', context)