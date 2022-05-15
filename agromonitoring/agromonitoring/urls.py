from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as swagger 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('monitoring.urls'), name='main'),   
    path('auth/', include('authU.urls'), name='authU'),
    path('api/v1/', include('api.urls'), name='api'),
]

urlpatterns += swagger