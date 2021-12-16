from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework import permissions
from .models import Registration, Hotels
from .serializers import HotelsSerializer, RegistrationSerializer
# Create your views here.

class RegistrationListApiView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = RegistrationSerializer
    def get_queryset(self):
        return Registration.objects.all()


class HotelsListApiView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = HotelsSerializer
    def get_queryset(self):
        return Hotels.objects.all()