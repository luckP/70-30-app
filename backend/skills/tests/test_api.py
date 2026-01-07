import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from skills.models import Category, Skill, UserSkill

User = get_user_model()

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user():
    return User.objects.create_user(username='user1', password='password123')

@pytest.fixture
def other_user():
    return User.objects.create_user(username='user2', password='password123')

@pytest.fixture
def category():
    return Category.objects.create(name='Music', icon='music-icon')

@pytest.fixture
def skill(category):
    return Skill.objects.create(name='Guitar', category=category)

@pytest.mark.django_db
def test_get_categories(api_client, category):
    url = reverse('category-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['name'] == 'Music'

@pytest.mark.django_db
def test_get_skills(api_client, skill):
    url = reverse('skill-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['name'] == 'Guitar'

@pytest.mark.django_db
def test_create_user_skill(api_client, user, skill):
    url = reverse('userskill-list')
    api_client.force_authenticate(user=user)
    data = {
        'skill_id': skill.id,
        'proficiency': 'INTERMEDIATE',
        'years_of_experience': 2
    }
    response = api_client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED
    assert UserSkill.objects.filter(user=user, skill=skill).exists()
    assert response.data['proficiency'] == 'INTERMEDIATE'

@pytest.mark.django_db
def test_filter_user_skills_me(api_client, user, other_user, skill):
    url = reverse('userskill-list')
    # Create skills for both users
    UserSkill.objects.create(user=user, skill=skill, proficiency='EXPERT')
    UserSkill.objects.create(user=other_user, skill=skill, proficiency='BEGINNER')

    api_client.force_authenticate(user=user)
    
    # Test ?user=me
    response = api_client.get(f"{url}?user=me")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['proficiency'] == 'EXPERT'

    # Test filter by ID
    response = api_client.get(f"{url}?user={other_user.id}")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['proficiency'] == 'BEGINNER'
