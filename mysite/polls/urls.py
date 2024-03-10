from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views 

app_name = "polls"
urlpatterns = [
    path('', views.IndexView.as_view(), name="home"),
    path('register/', views.register, name='register'),
    path('login/', views.CustomLoginView.as_view(template_name='polls/login.html'), name='login'),
    path('account/', views.account, name='account'),
    path('change_password/', auth_views.PasswordChangeView.as_view()),
    path('logout/', views.logout_user, name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


