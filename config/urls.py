from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('app_pages.urls')),
    path('cars/', include('super_cars.urls')),
    path('accounts/', include('users.urls')),
    
]
