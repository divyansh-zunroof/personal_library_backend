from django.contrib import admin
from .models import UserInformation, Book

# Register your models here.
admin.site.register(UserInformation)
admin.site.register(Book)