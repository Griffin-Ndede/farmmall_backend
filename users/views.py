from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, viewsets
from .serializers import UserRegistrationSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .models import PotatoCrop
from .serializers import PotatoCropSerializer

class RegisterView(APIView):
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
    


class Crop(APIView):
    def post(self, request):
        """Handles POST requests for creating a new potato crop."""
        serializer = PotatoCropSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        """Handles GET requests for retrieving all potato crops."""
        crops = PotatoCrop.objects.all()
        serializer = PotatoCropSerializer(crops, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PotatoCropViewSet(viewsets.ModelViewSet):
    queryset = PotatoCrop.objects.all()
    serializer_class = PotatoCropSerializer