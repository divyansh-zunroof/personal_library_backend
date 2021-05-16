from django.urls import path
from . import views

urlpatterns = [
    path('login', views.loginUser, name='Login User'),
    path('create', views.createUser, name='Create User'),
    path('get_books', views.getBooks, name='Get Books'),
    path('add_books', views.addBooks, name='Add Books'),
]