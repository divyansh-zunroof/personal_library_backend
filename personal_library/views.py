from typing import cast
from django.http import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserInformation, Book
from rest_framework.decorators import api_view
import random
import string

# printing lowercase
letters = string.ascii_lowercase

# Create your views here.

@api_view(['GET', 'POST'])
def loginUser(request):
    """
    API Endpoint for logging in the user into the library\n
    Example request body:\n
    {\n
        "email": "JohnDoe@example.com",
        "password": "password@123"
    }\n
    """
    if request.method == 'POST':
        data = request.data
        userEmail = data['email']
        password = data['password']
        try:
            User = UserInformation.objects.get(email=userEmail)
            if User.password == password:
                loginHash = ''.join(random.choice(letters) for i in range(10))
                User.loginSessionHash = loginHash
                User.save()
                return Response({'login': 'verified', 'hash': loginHash})
            else:
                return Response({'login': 'not verified'})
        except UserInformation.DoesNotExist:
            return Response({'login': 'user undefined'})
    else:
        return Response({'error': 'request type not specified'})

@api_view(['GET', 'POST'])
def createUser(request):
    """
    API Endpoint for signing up the user into the library\n
    Example request body:\n
    {\n
        "fname": "John",
        "lname": "Doe",
        "email": "JohnDoe@example.com",
        "phone": "1234567890",
        "country": "India",
        "password": "password@123"
    }\n
    """
    if request.method == 'POST':
        data = request.data
        fname = data['fname']
        lname = data['lname']
        email =  data['email']
        phn = data['phone']
        country = data['country']
        password = data['password']

        User = UserInformation.objects.create(fname=fname,
        lname=lname, email=email, phn=phn, country=country, password=password)
        User.save()

        response = {
            'status': 'successfull',
            'email': User.email,
            'fname': User.fname,
            'lname': User.lname
        }

        return Response(response)

    else:
        return Response({'error': 'request type not specified'})


@api_view(['POST'])
def getBooks(request):
    """
    API Endpoint for getting books of the current user from the library\n
    Example request body:\n
    {\n
        "email": "JohnDoe@example.com",
        "hash": "twghdcjbeyr"
    }\n
    """
    if request.method == 'POST':
        userHash = request.data['hash']
        email = request.data['email']
        User = UserInformation.objects.get(loginSessionHash=userHash)
        if User.email == email:
            books = Book.objects.all().filter(holder = User)
            book_list = []
            for book_itr in books:
                book = {
                'title': book_itr.title,
                'pages': book_itr.pages,
                'author': book_itr.author,
                'url': book_itr.url,
                }
                book_list.append(book)
            print('sending books')
            return Response({'book_list': book_list})


@api_view(['POST'])
def addBooks(request):
    """
    API Endpoint for adding books of the current user in the library.\n
    Example request body:\n
    {\n
        "email": "JohnDoe@example.com",
        "hash": "twghdcjbeyr",
        "title": "Example",
        "author": "Example author",
        "pages": "250",
        "url": "www.example.com"
    }\n
    """
    if request.method == 'POST':
        userHash = request.data['hash']
        email = request.data['email']

        User = UserInformation.objects.get(loginSessionHash=userHash)

        title = request.data['title']
        pages = request.data['pages']
        author = request.data['author']
        url = request.data['url']
        if User.email == email:
            book = Book(title=title, holder=User, pages=pages, author=author, url=url)
            book.save()
            return Response({'status': 'successfull'})




        