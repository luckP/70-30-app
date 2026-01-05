import pytest
from users.models import User

@pytest.fixture
def user_data():
    return {
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'testpassword123',
        'user_type': User.UserType.MENTEE
    }

@pytest.fixture
def mentor_data():
    return {
        'username': 'mentoruser',
        'email': 'mentor@example.com',
        'password': 'testpassword123',
        'user_type': User.UserType.MENTOR
    }
