from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # Include your app's URLs
    path('metrics/', include('django_prometheus.urls')),  # This is crucial for exposing /metrics/
]
