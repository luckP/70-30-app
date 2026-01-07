from django.contrib import admin
from .models import Category, Skill, UserSkill

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon', 'created_at')
    search_fields = ('name',)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'created_at')
    list_filter = ('category',)
    search_fields = ('name', 'category__name')

@admin.register(UserSkill)
class UserSkillAdmin(admin.ModelAdmin):
    list_display = ('user', 'skill', 'proficiency', 'years_of_experience')
    list_filter = ('proficiency', 'skill__category')
    search_fields = ('user__username', 'user__email', 'skill__name')
    autocomplete_fields = ['user', 'skill']
