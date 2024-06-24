from django.urls import path
from . import views

urlpatterns = [
    path('', views.user, name='register'),  # Corrected path with an empty string
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
]
