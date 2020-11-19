from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Wallet(models.Model):
    user = models.OneToOneField('user.User', on_delete=models.CASCADE)
    amount = models.FloatField(default=0)

    def __str__(self):
        return '{}-{}'.format(self.user.username, self.amount)

    class Meta:
        verbose_name = 'wallet'
        verbose_name_plural = 'wallets'


class User(AbstractUser):
    address = models.CharField(max_length=255, null=True)
    phone = models.IntegerField(null=True)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.username
