from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from .models import Activity



User = get_user_model()

class HomeSerializer(serializers.Serializer):
    message = serializers.CharField()
    
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

    
class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for user profile data.
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class UserLoginSerializer(serializers.Serializer):
    """
    Serializer for user login.
    """
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'user', 'crop_name', 'activity', 'activity_date']
        read_only_fields = ['id', 'user']  # User is automatically set in the view