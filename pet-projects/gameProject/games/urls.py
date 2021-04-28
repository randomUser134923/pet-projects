from django.urls import path

from . import views

urlpatterns = [
    path('',views.guessnumber, name='guessnumber'),

    
]