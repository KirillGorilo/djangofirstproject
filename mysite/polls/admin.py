from django.contrib import admin
from polls.models import ToDoItem, ToDoList

admin.site.register(ToDoItem)
admin.site.register(ToDoList)