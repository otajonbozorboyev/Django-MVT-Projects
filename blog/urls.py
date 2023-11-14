from django.urls import path
from .views import indexView, aboutView, detailView, blogView, contactView

urlpatterns = [
    path('', indexView, name='index'),
    path('blog/<int:pk>/', detailView, name='detail'),
    path('about/', aboutView, name='abouts'),
    path('blog/', blogView, name='blog'),
    path('contact/', contactView, name='contact')
]