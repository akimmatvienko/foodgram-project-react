from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.conf import settings

from .validators import validate_me_name


class User(AbstractUser):
    """User setting model"""

    username_validator = UnicodeUsernameValidator()
    email = models.EmailField(
        help_text='Ваш электронный адрес',
        verbose_name='Электронная почта',
        max_length=settings.EMAIL_LENGTH,
        unique=True,
    )

    username = models.CharField(
        help_text='Ваш логин',
        verbose_name='Логин',
        max_length=settings.USER_FIELD_LENGTH,
        unique=True,
        validators=[username_validator, validate_me_name],
    )
    first_name = models.CharField(
        help_text='Ваше имя',
        verbose_name='Имя',
        max_length=settings.USER_FIELD_LENGTH,
    )
    last_name = models.CharField(
        help_text='Ваша фамилия',
        verbose_name='Фамилия',
        max_length=settings.USER_FIELD_LENGTH,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = 'username', 'first_name', 'last_name'

    class Meta:
        ordering = ['username']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Subscribe(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='subscriber',
        verbose_name='Пользователь'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='subscribing',
        verbose_name='Автор'
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'author'],
                name='unique_subscribe'
            ),
            models.CheckConstraint(
                check=~models.Q(user=models.F('author')),
                name='self_subscribe'
            ),
        ]

    def __str__(self):
        return f'{self.user}-{self.author}'
