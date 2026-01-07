import pytest
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError
from skills.models import Category, Skill, UserSkill

User = get_user_model()

@pytest.fixture
def user():
    return User.objects.create_user(username='testuser', password='password')

@pytest.fixture
def category():
    return Category.objects.create(name='Technology', icon='tech-icon')  # pylint: disable=no-member

@pytest.fixture
def skill(category):
    return Skill.objects.create(name='Python', category=category)  # pylint: disable=no-member

@pytest.mark.django_db
def test_category_str(category):
    assert str(category) == 'Technology'

@pytest.mark.django_db
def test_skill_str(skill):
    assert str(skill) == 'Python'

@pytest.mark.django_db
def test_user_skill_creation_and_str(user, skill):
    user_skill = UserSkill.objects.create(  # pylint: disable=no-member
        user=user,
        skill=skill,
        proficiency=UserSkill.Proficiency.EXPERT,
        years_of_experience=5,
        description="I love coding"
    )
    assert str(user_skill) == "testuser - Python (Expert)"
    assert user_skill.years_of_experience == 5

@pytest.mark.django_db
def test_user_skill_unique_constraint(user, skill):
    UserSkill.objects.create(  # pylint: disable=no-member
        user=user,
        skill=skill,
        proficiency=UserSkill.Proficiency.BEGINNER
    )
    with pytest.raises(IntegrityError):
        UserSkill.objects.create(  # pylint: disable=no-member
            user=user,
            skill=skill,
            proficiency=UserSkill.Proficiency.EXPERT
        )
