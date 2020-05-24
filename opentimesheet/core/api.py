from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()

app_name = "api"
urlpatterns = [
    path("auth/token", TokenObtainPairView.as_view(), name="auth_token"),
    path("auth/token/refresh", TokenRefreshView.as_view(), name="auth_token_refresh"),
]
urlpatterns += router.urls
