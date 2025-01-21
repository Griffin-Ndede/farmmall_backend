from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, viewsets
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .models import PotatoCrop, User
from .serializers import UserRegistrationSerializer, PotatoCropSerializer, UserLoginSerializer, CalendarEventSerializer
from django.contrib.auth import authenticate
from rest_framework import status
from .models import CalendarEvent

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

class Crop(APIView):
    """
    Handles POST and GET for PotatoCrop data.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PotatoCropSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        crops = PotatoCrop.objects.all()
        serializer = PotatoCropSerializer(crops, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PotatoCropViewSet(viewsets.ModelViewSet):
    """
    CRUD operations for PotatoCrop using ViewSet.
    """
    queryset = PotatoCrop.objects.all()
    serializer_class = PotatoCropSerializer



class CalendarEventView(APIView):
    def get(self, request):
        events = CalendarEvent.objects.all()
        serializer = CalendarEventSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CalendarEventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)