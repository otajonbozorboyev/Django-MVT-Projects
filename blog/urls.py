from django.urls import path
from .views import indexView, blogView, detailView

urlpatterns = [
    path('', indexView, name='index'),
    path('blog/', blogView, name='blog'),
    path('blog/<int:pk>/', detailView, name='detail')
]