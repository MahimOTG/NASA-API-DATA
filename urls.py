from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('get_nasa_data/', views.get_nasa_data, name='get_nasa_data'),  # Fetch NASA data
    path('download_nasa_data/', views.download_nasa_data, name='download_nasa_data'),  # Download NASA data
]

