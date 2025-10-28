from django.contrib import admin
from .models import Author, Category, event


admin.site.register(Author)
admin.site.register(Category)
admin.site.register(event)
