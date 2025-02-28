from django.urls import path
from .views import RegisterView, LoginView, ActivityView, UserProfileView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('activities/', ActivityView.as_view(), name='activity-list'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),

]
