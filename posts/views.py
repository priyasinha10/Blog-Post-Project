from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import BlogPost
from .serializers import BlogPostSerializer
from .permissions import IsAuthorOrReadOnly
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    """
    Custom JWT login view to avoid 403 CSRF issues.
    """
    serializer_class = TokenObtainPairSerializer

class BlogPostViewSet(viewsets.ModelViewSet):
    """
    ViewSet for CRUD operations on BlogPost.
    - Any user can read posts
    - Only authenticated authors can create/update/delete their own posts
    """
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    # Enable searching by title/content
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        """
        Automatically set the author of the post to the logged-in user.
        """
        serializer.save(author=self.request.user)
