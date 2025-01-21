from django.urls import path
from .views import RegisterView, LoginView, Crop, CalendarEventView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('potato/', Crop.as_view(), name='potato'),
    path('events/', CalendarEventView.as_view(), name='calendar-events'),
]
