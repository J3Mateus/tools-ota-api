import uuid

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager as BUM
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from apps.common.models.base_model import BaseModel
from utils import remove_special_characters
# Taken from here:
# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#a-full-example
# With some modifications


class BaseUserManager(BUM):
    def create_user(self,username, email,phone,whatsapp,full_name,created_by=None,deleted_by=None, is_active=True, is_admin=False, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(username=username,
                        email=self.normalize_email(email.lower()),
                        phone=phone,
                        whatsapp=whatsapp,
                        full_name=full_name,
                        created_by=created_by,
                        deleted_by=deleted_by,
                        is_active=is_active,
                        is_admin=is_admin,
                        )

        if password is not None:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.full_clean()
        user.save(using=self._db)

        return user

    def create_superuser(self,username,email,phone,whatsapp, full_name, password=None):
        user = self.create_user(
            username=username,
            email=email,
            phone=phone,
            whatsapp=whatsapp,
            full_name=full_name,
            is_active=True,
            is_admin=True,
            password=password,
        )

        user.is_superuser = True
        user.save(using=self._db)

        return user


class BaseUser(BaseModel, AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    username = models.CharField(null=False,unique=True,verbose_name='username')
    phone = models.CharField(null=True,verbose_name='phone')
    whatsapp = models.CharField(null=True,verbose_name='whatsapp')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    full_name = models.CharField(verbose_name="Nome completo do usuário",max_length=250,null=True,blank=True)
    # This should potentially be an encrypted field
    jwt_key = models.UUIDField(default=uuid.uuid4)

    objects = BaseUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['full_name','phone','whatsapp','email']

    def __str__(self):
        return self.username

    def get_full_name(self):
        return f'{self.full_name}'

    def is_staff(self):
        return self.is_admin
