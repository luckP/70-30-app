import pytest
from users.models import User, Profile

@pytest.mark.django_db
class TestProfileModel:
    def test_create_profile(self):
        user = User.objects.create_user(username='profileuser', password='password')
        profile = Profile.objects.create(user=user, bio="Test Bio")
        
        assert profile.user == user
        assert profile.bio == "Test Bio"
        assert str(profile) == "profileuser's Profile"

    def test_profile_one_to_one(self):
        user = User.objects.create_user(username='unique', password='password')
        Profile.objects.create(user=user)
        
        # Verify related name
        assert hasattr(user, 'profile')
        assert user.profile is not None
