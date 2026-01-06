from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.exceptions import TokenError

from .serializers import (
    UserSerializer, 
    LogoutSerializer, 
    ProfileSerializer, 
    LocationUpdateSerializer
)
from .models import Profile

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer

    @swagger_auto_schema(
        tags=['Authentication'],
        operation_description="Register a new user (Mentor or Mentee).",
        responses={
            201: UserSerializer,
            400: "Bad Request - Invalid Input"
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class LogoutView(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = LogoutSerializer

    @swagger_auto_schema(
        tags=['Authentication'],
        operation_description="Blacklist the refresh token to logout user.",
        request_body=LogoutSerializer,
        responses={
            205: "Reset Content - Successfully logged out",
            400: "Bad Request - Invalid or missing token"
        }
    )
    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            if not refresh_token:
                 return Response({"error": "Refresh token is required"}, status=status.HTTP_400_BAD_REQUEST)
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except TokenError:
            return Response({"error": "Invalid refresh token"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
             return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)  # pylint: disable=no-member

    def get_object(self):
        # Ensure profile exists (it should due to signals, but safety check)
        # Note: We haven't implemented the signal yet, so we might need get_or_create here
        # strictly for robustness if the signal isn't there.
        # But standard pattern is just get_object returning the instance.
        # If we use get_object_or_404 on the queryset filtered by user, it should work.
        obj, created = Profile.objects.get_or_create(user=self.request.user)  # pylint: disable=no-member
        return obj

    @swagger_auto_schema(
        tags=['Profile'],
        operation_description="Retrieve or update the authenticated user's profile.",
        responses={200: ProfileSerializer}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Profile'],
        operation_description="Update profile fields (bio, avatar, experience, location).",
        responses={200: ProfileSerializer}
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)


class LocationUpdateView(generics.UpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = LocationUpdateSerializer
    http_method_names = ['patch']

    def get_object(self):
        obj, created = Profile.objects.get_or_create(user=self.request.user)  # pylint: disable=no-member
        return obj

    @swagger_auto_schema(
        tags=['Profile'],
        operation_description="Update the user's geographical location using latitude and longitude.",
        responses={200: LocationUpdateSerializer}
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
