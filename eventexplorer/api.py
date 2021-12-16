from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('rest_framework.urls')),
    path('congress/', include('congress.api'))
]