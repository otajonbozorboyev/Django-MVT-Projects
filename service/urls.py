from django.urls import path
from .views import serviceView

urlpatterns =[
    path('', serviceView, name="service")

]