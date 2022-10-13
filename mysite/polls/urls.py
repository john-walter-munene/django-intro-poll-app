from xml.etree.ElementInclude import include
from django.urls import  path, include
from . import views

# Begin mapping my urls
urlpatterns = [
    path('', views.index, name="index")
]
