from django.urls import path
from . import views
urlpatterns = [
    #path function defines a url pattern....
    path('', views.index, name='index'),
]