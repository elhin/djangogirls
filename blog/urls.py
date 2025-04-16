from django.urls import path
# . means current folder
from . import views

urlpatterns = [
    #path that takes 3 arguments, path url, function u want to run when you go to url and if u want to create a 
    #separate name for the function that the view can use
    path('', views.post_list, name='post_list')
]