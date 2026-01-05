import pytest
from users.models import User

@pytest.mark.django_db
def test_create_user(user_data):
    user = User.objects.create_user(**user_data)
    assert user.username == user_data['username']
    assert user.email == user_data['email']
    assert user.check_password(user_data['password'])
    assert user.user_type == User.UserType.MENTEE
    assert str(user) == f"{user.username} (Mentee)"

@pytest.mark.django_db
def test_create_mentor(mentor_data):
    user = User.objects.create_user(**mentor_data)
    assert user.user_type == User.UserType.MENTOR
    assert str(user) == f"{user.username} (Mentor)"

@pytest.mark.django_db
def test_create_superuser(user_data):
    # Ensure user_type defaults to ADMIN even if not provided or provided incorrectly
    if 'user_type' in user_data:
        del user_data['user_type']
    
    admin = User.objects.create_superuser(**user_data)
    assert admin.is_superuser
    assert admin.is_staff
    assert admin.user_type == User.UserType.ADMIN
