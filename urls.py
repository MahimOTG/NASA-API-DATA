
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('nasa_app.urls')),  # This includes all the URLs from the nasa_app
]
