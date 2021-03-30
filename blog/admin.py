from django.contrib import admin
from .models import Post # importing Post here


# Register your models here.
admin.site.register(Post) # we do this to show Post model in our admin panel

