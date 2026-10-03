from django.contrib import admin

from .models import Course, Student, Book, Genre

admin.site.register([Course, Student, Book, Genre])
