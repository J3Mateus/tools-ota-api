from typing import Optional

from django.db import transaction
from django.contrib.auth.hashers import make_password
from apps.users.models import BaseUser


@transaction.atomic
def user_create(
    *, email: str,phone: str,
    whatsapp: str, 
    is_active: bool = True, 
    is_admin: bool = False,
    full_name: str, 
    created_by: BaseUser,
    password: Optional[str] = None
) -> BaseUser:    
    user = BaseUser.objects.create(email=email,
                                  phone=phone,
                                  whatsapp=whatsapp,
                                  full_name=full_name,
                                  created_by=None,
                                  is_active=is_active, 
                                  is_admin=is_admin,
                                  password=make_password(password)
                                  )
    
    user.save()
    return user
