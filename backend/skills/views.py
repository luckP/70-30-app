# pylint: disable=no-member 

from rest_framework import viewsets, permissions, filters
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Category, Skill, UserSkill
from .serializers import CategorySerializer, SkillSerializer, UserSkillSerializer

@swagger_auto_schema(tags=['Categories'])
class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

@swagger_auto_schema(tags=['Skills'])
class SkillViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows skills to be viewed or edited.
    """
    queryset = Skill.objects.all().order_by('name')
    serializer_class = SkillSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'category__name']

@swagger_auto_schema(tags=['User Skills'])
class UserSkillViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to manage their own skills.
    Use ?user=me to filter by current user, or ?user=<id> for specific user.
    """
    serializer_class = UserSkillSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = UserSkill.objects.all().select_related('skill', 'skill__category', 'user')
        
        user_param = self.request.query_params.get('user')
        if user_param == 'me':
            return queryset.filter(user=self.request.user)
        elif user_param:
            return queryset.filter(user__id=user_param)
            
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'user', 
                openapi.IN_QUERY, 
                description="Filter by user ID or 'me' for current user", 
                type=openapi.TYPE_STRING
            )
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
