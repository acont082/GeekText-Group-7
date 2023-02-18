from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    home_address = models.CharField(max_length=255, null=True, blank=True)
    groups = models.ManyToManyField('auth.Group', related_name='auth_user_groups', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='auth_user_permissions', blank=True)

    def __str__(self):
        return self.username

    class Meta:
        app_label = 'bookstore_api'


class CreditCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='credit_cards')
    card_number = models.CharField(max_length=16)
    card_type = models.CharField(max_length=255)
    expiration_date = models.DateField()

    class Meta:
        app_label = 'bookstore_api'

    def __str__(self):
        return self.card_number
