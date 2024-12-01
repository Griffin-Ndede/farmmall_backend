from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from .models import PotatoCrop

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for registering a new user.
    """
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']

    def validate_password(self, value):
        return make_password(value)  # Hash the password

    def create(self, validated_data):
        return User.objects.create(**validated_data)

class UserLoginSerializer(serializers.Serializer):
    """
    Serializer for user login.
    """
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)

class PotatoCropSerializer(serializers.ModelSerializer):
    """
    Serializer for PotatoCrop model.
    """
    class Meta:
        model = PotatoCrop
        fields = ['activity', 'date', 'county', 'fertilizer_type', 'irrigation_used', 'notes']
