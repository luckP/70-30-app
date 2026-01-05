"""
User model that extends AbstractUser with additional fields.
"""
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user manager to handle user creation with specific types.
    """
    def create_user(self, username, email=None, password=None, **extra_fields):
        if not username:
            raise ValueError(_('The Username field must be set'))
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        # Ensure superusers are always set to ADMIN type
        extra_fields.setdefault('user_type', User.UserType.ADMIN)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    """
    User model that extends AbstractUser with additional fields.
    """
    class UserType(models.TextChoices):
        """
        Enumeration for user types available in the system.
        """
        MENTOR = 'MENTOR', _('Mentor')
        MENTEE = 'MENTEE', _('Mentee')
        ADMIN = 'ADMIN', _('Admin')

    user_type = models.CharField(
        max_length=10,
        choices=UserType.choices,
        default=UserType.MENTEE,
        verbose_name=_("User Type")
    )

    objects = CustomUserManager()

    def __str__(self):
        # pylint: disable=no-member
        return f"{self.username} ({self.get_user_type_display()})"
