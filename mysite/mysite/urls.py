from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("rozanov/", include("polls.urls")),
    path('admin/', admin.site.urls),
]
