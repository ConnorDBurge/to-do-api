from django.contrib import admin
from .models import UserProfile, ToDoItem

admin.site.register(UserProfile)
admin.site.register(ToDoItem)