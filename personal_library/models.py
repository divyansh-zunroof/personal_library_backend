from django.db import models

# Create your models here.

class UserInformation(models.Model):
    fname = models.CharField(max_length=250)
    lname = models.CharField(max_length=250)
    email = models.EmailField()
    phn = models.CharField(max_length=10)
    country = models.CharField(max_length=25)
    password = models.CharField(max_length=250)
    loginSessionHash = models.CharField(max_length=10, default="##########");

    def __str__(self):
        return self.fname+" "+self.lname

class Book(models.Model):
    
    title = models.CharField(max_length=250)
    pages = models.CharField(max_length=20)
    author = models.CharField(max_length=250)
    holder = models.ForeignKey(UserInformation, on_delete=models.CASCADE)
    url = models.URLField()

    def __str__(self):
        return self.title
