from django.urls import path 
from .views import cars_list
from . import views

urlpatterns = [
    path('', cars_list, name='cars_list'),
    # path('add/', views.add_car, name='add_car'),

]