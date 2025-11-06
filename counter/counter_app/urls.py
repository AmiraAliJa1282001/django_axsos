from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('destroy_session', views.destroy, name='destroy'),
    path('plus_two', views.plus_two, name='plus_two'),          # NINJA bonus
    path('custom_increment', views.custom_increment, name='custom_increment'),  # SENSEI bonus
]
