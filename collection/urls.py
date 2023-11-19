from django.urls import path
from .views import collectionView

urlpatterns =[
    path('', collectionView, name="collection"),
]
