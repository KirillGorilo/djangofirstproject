from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views 

app_name = "polls"
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path("accounts/login/", auth_views.LoginView.as_view(template_name="polls/logtest.html")),
    path("accounts/", include("django.contrib.auth.urls")),

]


