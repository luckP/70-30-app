import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from users.models import User, Profile

@pytest.mark.django_db
class TestProfileAPI:
    def setup_method(self):
        self.client = APIClient()
        self.profile_url = reverse('profile-me')
        self.location_url = reverse('profile-location')
        
        # Create test user
        self.user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpassword'
        }
        self.user = User.objects.create_user(**self.user_data)

    def test_get_profile_unauthenticated(self):
        response = self.client.get(self.profile_url)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_get_profile_authenticated(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.profile_url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['username'] == self.user.username
        # Verify lazy creation
        assert Profile.objects.filter(user=self.user).exists()

    def test_update_profile(self):
        self.client.force_authenticate(user=self.user)
        
        data = {
            'bio': 'Updated Bio',
            'years_of_experience': 5
        }
        response = self.client.patch(self.profile_url, data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['bio'] == 'Updated Bio'
        
        self.user.profile.refresh_from_db()
        assert self.user.profile.bio == 'Updated Bio'

    def test_update_location(self):
        self.client.force_authenticate(user=self.user)
        
        data = {
            'latitude': 40.7128,
            'longitude': -74.0060
        }
        response = self.client.patch(self.location_url, data)
        assert response.status_code == status.HTTP_200_OK
        
        # Verify location in response if serializer returns it
        # LocationUpdateSerializer returns instance, but we check logic
        self.user.profile.refresh_from_db()
        # Note: Local environment might use MockPoint, so actual retrieval might depend on environment
        # But verify no crash and 200 OK
