from typing import Any, Optional
from django.contrib.auth.models import AbstractUser, UserManager
from django.db.models import EmailField


class UserManagerWrapper(UserManager):
    def create_superuser(
        self,
        username: str,
        email: str | None,
        password: str | None,
        **extra_fields: Any
    ) -> Any:
        return super().create_superuser(email, email, password, **extra_fields)


class User(AbstractUser):
    email = EmailField(max_length=255, unique=True)

    objects = UserManagerWrapper()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    pass
