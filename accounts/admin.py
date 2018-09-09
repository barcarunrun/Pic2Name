# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import AbstractBaseUser, User
from .models import AuthUser

# Register your models here.
class AuthUserInline(admin.StackedInline):
    model = AuthUser
    can_delete = False
    verbose_name_plural = 'AuthUsers'

class UserAdmin(BaseUserAdmin):
    inlines = (AuthUserInline, )