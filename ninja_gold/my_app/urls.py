from django.urls import path     
from my_app import views
urlpatterns = [
    path('', views.index), 
    path('process_money',views.process_money),
    path('reset',views.reset)
    ]