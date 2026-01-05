from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    class UserType(models.TextChoices):
        MENTOR = 'MENTOR', _('Mentor')
        MENTEE = 'MENTEE', _('Mentee')
        ADMIN = 'ADMIN', _('Admin')

    user_type = models.CharField(
        max_length=10,
        choices=UserType.choices,
        default=UserType.MENTEE,
        verbose_name=_("User Type")
    )

    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"
