# pylint: disable=no-member 

from rest_framework import serializers
from .models import Category, Skill, UserSkill

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'icon', 'created_at', 'updated_at']

class SkillSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category', 
        write_only=True
    )
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Skill
        fields = ['id', 'name', 'category', 'category_id', 'created_at', 'updated_at']

class UserSkillSerializer(serializers.ModelSerializer):
    skill_id = serializers.PrimaryKeyRelatedField(
        queryset=Skill.objects.all(), 
        source='skill', 
        write_only=True
    )
    skill = SkillSerializer(read_only=True)
    user = serializers.StringRelatedField(read_only=True)
    proficiency_display = serializers.CharField(source='get_proficiency_display', read_only=True)

    class Meta:
        model = UserSkill
        fields = [
            'id', 'user', 'skill', 'skill_id', 
            'proficiency', 'proficiency_display', 
            'years_of_experience', 'description', 
            'created_at', 'updated_at'
        ]
        read_only_fields = ['user']
