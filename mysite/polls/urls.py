from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from . import views 

app_name = "polls"
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('register/', views.auth, name='auth')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


