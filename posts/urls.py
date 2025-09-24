from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogPostViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
router = DefaultRouter()
router.register(r'posts', BlogPostViewSet, basename='blogpost')

urlpatterns = [
    path('', include(router.urls)),
    path('jwt/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
