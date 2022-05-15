from django import views
from django.urls import path, include

from .views import LoginUser, logout_view

urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
]

