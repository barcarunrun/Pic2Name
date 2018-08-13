from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin



class AuthUserManager(BaseUserManager):
    def create_user(self, username, password):

        if not username:
            raise ValueError('Users must have an username')

        user = self.model(username=username,
                          password=password,
                          )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):

        user = self.create_user(username=username,
                                password=password
                                )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class AuthUser(AbstractBaseUser, PermissionsMixin):

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'user'

    def get_short_name(self):

        return self.username

    def get_full_name(self):
        return self.username

    def get_name(self):

        return self.username

    username = models.CharField(verbose_name='userID',
                                unique=True,
                                max_length=30)


    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(verbose_name='ActiveFlag',
                                    default=True)

    is_staff = models.BooleanField(verbose_name='AccessAuthority',
                                   default=False)
    USERNAME_FIELD = 'username'

    objects = AuthUserManager()

    def __str__(self):
        return self.username

class Result(models.Model):

    result1 = models.CharField(max_length=50,null='true')
    result2 = models.CharField(max_length=50,null='true')
    result3 = models.CharField(max_length=50,null='true')
    result4 = models.CharField(max_length=50,null='true')
    result5 = models.CharField(max_length=50,null='true')
    result6 = models.CharField(max_length=50,null='true')
    result7 = models.CharField(max_length=50,null='true')
    result8 = models.CharField(max_length=50,null='true')
    result9 = models.CharField(max_length=50,null='true')
    result10 = models.CharField(max_length=50,null='true')
    score1=models.DecimalField(max_digits=11, decimal_places=10,null='true')
    score2 = models.DecimalField(max_digits=11, decimal_places=10,null='true')
    score3 = models.DecimalField(max_digits=11, decimal_places=10,null='true')
    score4 = models.DecimalField(max_digits=11, decimal_places=10,null='true')
    score5 = models.DecimalField(max_digits=11, decimal_places=10,null='true')
    score6 = models.DecimalField(max_digits=11, decimal_places=10,null='true')
    score7 = models.DecimalField(max_digits=11, decimal_places=10,null='true')
    score8 = models.DecimalField(max_digits=11, decimal_places=10,null='true')
    score9 = models.DecimalField(max_digits=11, decimal_places=10,null='true')
    score10 = models.DecimalField(max_digits=11, decimal_places=10,null='true')

    result_from_user = models.CharField(max_length=50)
    result_time = models.DateTimeField(auto_now_add=True)
    file_name = models.CharField(max_length=50)


class FileNameModel(models.Model):
    file_name = models.CharField(max_length = 50)
    upload_time = models.DateTimeField(auto_now_add=True)
    userID=models.CharField(max_length = 50)
    result = models.ForeignKey(Result)

#class Photo(models.Model):
 #   image = models.ImageField(upload_to='myapp')
  #  file_name = models.CharField(max_length=50)
   # upload_time = models.DateTimeField(auto_now_add=True)
    #userID = models.CharField(max_length=30)
