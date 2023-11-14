from django.shortcuts import redirect, render
from .models import About, Blog, Skill
from .forms import ContactForm, SubscribeForm, CommentForm

# Create your views here.

def indexView(request):
    blog = Blog.objects.all().order_by('-id')[:5]
    about = About.objects.all()
    context = {
        'abouts': about,
        'blogs': blog,
    }
    return render(request, 'index.html', context)



def detailView(request, pk):
    about = About.objects.all()
    blog = Blog.objects.get(id=pk)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        com = form.save(commit=False)
        com.blog = blog
        com.save()
        return redirect('.')
    context = {
        'form': form,
        'abouts': about,
        'detail': blog
    }
    return render(request, 'single.html', context)



def aboutView(request):
    about = About.objects.all()
    skill = Skill.objects.all()
    context = {
        'abouts': about,
        'skill': skill
    }
    return render(request, 'about.html', context)



def blogView(request):
    blog = Blog.objects.all().order_by('-id')
    about = About.objects.all()
    context = {
        'abouts': about,
        'blogs': blog
    }
    return render(request, 'blog.html', context)



def contactView(request):
    form = ContactForm(request.POST or None)
    about = About.objects.all()
    if form.is_valid():
        form.save()
        # return redirect('/contact/')
    context = {
        'form': form,
        'abouts': about
    }

    return render(request, 'contact.html', context)


