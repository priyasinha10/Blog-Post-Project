from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


class BlogPostAPITests(APITestCase):
    """
    Test cases for Blog API with JWT authentication.
    """

    def setUp(self):
        """
        Create two users and a sample blog post.
        """
        self.user = User.objects.create_user(username="author", password="password123")
        self.other_user = User.objects.create_user(username="reader", password="password123")

        self.post = self.user.posts.create(
            title="First Blog",
            content="This is a test blog content"
        )

        self.client = APIClient()

    def get_jwt_token(self, user):
        """
        Helper: Generate a JWT token for a user.
        """
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

    def authenticate(self, user=None):
        """
        Authenticate requests with JWT token.
        """
        token = self.get_jwt_token(user or self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    def test_jwt_authentication_valid(self):
        """Valid JWT allows access"""
        self.authenticate()
        response = self.client.get("/api/posts/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post_authenticated(self):
        """Authenticated users can create posts"""
        self.authenticate()
        data = {"title": "New Blog", "content": "New blog content"}
        response = self.client.post("/api/posts/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_post_unauthenticated(self):
        """Unauthenticated users cannot create posts"""
        data = {"title": "New Blog", "content": "New blog content"}
        response = self.client.post("/api/posts/", data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_post_author(self):
        """Author can update"""
        self.authenticate(self.user)
        data = {"title": "Updated Blog", "content": "Updated content"}
        response = self.client.put(f"/api/posts/{self.post.id}/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_post_non_author(self):
        """Non-author cannot update"""
        self.authenticate(self.other_user)
        data = {"title": "Hacked Blog", "content": "Not allowed"}
        response = self.client.put(f"/api/posts/{self.post.id}/", data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_post_author(self):
        """Author can delete"""
        self.authenticate(self.user)
        response = self.client.delete(f"/api/posts/{self.post.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_post_non_author(self):
        """Non-author cannot delete"""
        self.authenticate(self.other_user)
        response = self.client.delete(f"/api/posts/{self.post.id}/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
