from django.urls import path
from .views import aboutView

urlpatterns = [
    path('', aboutView, name='abouts')
]
