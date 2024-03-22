from django.urls import path
from .views import register_view

urlpatterns = [
    path('register/', register_view, name='register_page'),
    # path('login/', views.login_request, name='login'),
    # path('logout/', views.logout_request, name='logout'),
]
