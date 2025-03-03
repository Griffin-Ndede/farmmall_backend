from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status, viewsets
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User, Activity
from .serializers import UserRegistrationSerializer, UserLoginSerializer, ActivitySerializer, UserProfileSerializer
from django.contrib.auth import authenticate
from datetime import timedelta


class UserProfileView(APIView):
    """
    Retrieve logged-in user details.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserProfileSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RegisterView(APIView):
    """
    Handles user registration.
    """
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    """
    Handles user login.
    """
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }, status=status.HTTP_200_OK)
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActivityView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Fetch activities only for the logged-in user
        activities = Activity.objects.filter(user=request.user)
        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ActivitySerializer(data=request.data)
        if serializer.is_valid():
            activity = serializer.save(user=request.user)  # Set user here

            # Projected events logic
            if activity.activity.lower() == "planting":
                planting_date = activity.activity_date
                projected_events = [
                    Activity(
                        user=request.user,
                        crop_name=activity.crop_name,
                        activity="Weeding",
                        activity_date=planting_date + timedelta(weeks=3),
                    ),
                    Activity(
                        user=request.user,
                        crop_name=activity.crop_name,
                        activity="Harvesting",
                        activity_date=planting_date + timedelta(weeks=12),
                    ),
                ]
                Activity.objects.bulk_create(projected_events)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
