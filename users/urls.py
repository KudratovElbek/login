from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    # path('login/', views.login_request, name='login'),
    # path('logout/', views.logout_request, name='logout'),
]
