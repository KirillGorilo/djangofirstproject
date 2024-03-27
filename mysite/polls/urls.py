from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views 

app_name = "polls"
urlpatterns = [
    path('', views.ListListView.as_view(), name="home"),
    path('register/', views.register, name='register'),
    path('login/', views.CustomLoginView.as_view(template_name='polls/login.html'), name='login'),
    path('account/', views.account, name='account'),
    path('change_password/', auth_views.PasswordChangeView.as_view()),
    path('logout/', views.logout_user, name='logout'),    
    path("list/<int:list_id>/", views.ItemListView.as_view(), name="list"),
    path("list/add/", views.ListCreate.as_view(), name="list-add"),
    path("list/<int:list_id>/item/add/", views.ItemCreate.as_view(), name="item-add"),
    path("list/<int:list_id>/item/<int:pk>/", views.ItemUpdate.as_view(), name="item-update"),
    path("list/<int:pk>/delete/", views.ListDelete.as_view(), name="list-delete"),
    path("list/<int:list_id>/item/<int:pk>/delete/", views.ItemDelete.as_view(), name="item-delete"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


