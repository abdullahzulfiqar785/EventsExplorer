from django.db.models import fields
from rest_framework import serializers
from .models import Registration, Hotels


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = "__all__"


class HotelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotels
        fields = "__all__"