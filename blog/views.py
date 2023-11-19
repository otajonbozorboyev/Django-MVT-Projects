from django.shortcuts import redirect, render
from about.models import About
from collection.models import Collection
from contact.models import ContactMe
from .models import Blog, Category, Tag
from .forms import CommentForm, SubscribeForm
from django.core.paginator import Paginator



def indexView(request):
    contactme = ContactMe.objects.all()
    about = About.objects.all()
    collection = Collection.objects.all().order_by('-id')[:5]
    category = Category.objects.all()
    blog = Blog.objects.all().order_by('-id')
    context = {
        'abouts': about,
        'cme': contactme,
        'categories': category,
        'blogs': blog,
        'collections': collection
    }
    return render(request, 'index.html', context)


def blogView(request):
    collection = Collection.objects.all()
    about = About.objects.all()
    contactme = ContactMe.objects.all()
    category = Category.objects.all()
    tag = Tag.objects.all()
    blog = Blog.objects.all().order_by('-id')
    p = Paginator(blog, 1)
    page = request.GET.get('page')
    blog = p.get_page(page)
    popular = Blog.objects.order_by('-id')[:3]
    cat = request.GET.get('cat')
    form = SubscribeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('.')
    if cat:
        blog = blog.filter(category__title__iexact=cat)
    context = {
        'abouts': about,
        'collections': collection,
        'cme': contactme,
        'categories': category,
        'tags': tag,
        'blogs': blog,
        'populars':popular,
        'form': form
    }
    return render(request, 'blog.html', context)


def detailView(request, pk):
    about = About.objects.all()
    category = Category.objects.all()
    popular = Blog.objects.order_by('-id')[:3]
    tag = Tag.objects.all()
    blog = Blog.objects.get(id=pk)
    form = CommentForm(request.POST or None)
    cat = request.GET.get('cat')
    if cat:
        blog = blog.filter(category__title__iexact=cat)
    if form.is_valid():
        com = form.save(commit=False)
        com.blog = blog
        com.save()
        return redirect('.')
    context = {
    'blog': blog,
    'categories': category,
    'populars':popular,
    'tags': tag,
    'abouts': about,
    'form': form
    }
    return render(request, 'single.html', context)

