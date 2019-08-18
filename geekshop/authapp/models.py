from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class ShopUser(AbstractUser):
    # class Meta:
    #     verbose_name = 'пользователь'
    #     verbose_name_pluar = 'пользователи'

        avatar = models.ImageField(upload_to='user_avatar', blank=True)
        age = models.PositiveIntegerField(verbose_name='возраст')

        # def __str__(self):
        #     return self.username