from django.contrib import admin
from django.urls import path, include
from .views import RegistrationListApiView, HotelsListApiView

urlpatterns = [
    # path('hotels', ),
    path('registration/', RegistrationListApiView.as_view()),
    path('hotels/', HotelsListApiView.as_view())
]