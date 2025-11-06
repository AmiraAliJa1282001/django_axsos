from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path("", views.index, name='main'),
    path("register", views.register, name='register'),
    path("login", views.login, name='login'),
    path("success", views.success, name='success'),
    path("logout", views.logout, name='logout'),
]
