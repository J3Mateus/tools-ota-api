from django.db import models

from apps.common.models.base_model import BaseModel
#from apps.users.models import BaseUser

class Roles(BaseModel):
    
    ADMIN_CODE = "ADMIN"
    AGENT_CODE = "AGENT"
    TEACHER_CODE = "TEACHER"

    ROLES_CODE = [
        (ADMIN_CODE, "ADMIN"),
        (AGENT_CODE, "AGENT"),
        (TEACHER_CODE, "TEACHER"),
    ]
    
    ADMIN_NAME = "ADMINISTRADOR"
    AGENT_NAME = "AGENTE"
    TEACHER_NAME = "PROFESSOR"

    ROLES_NAME = [
        (ADMIN_NAME, "ADMINISTRADOR"),
        (AGENT_NAME, "AGENTE"),
        (TEACHER_NAME, "PROFESSOR"),
    ]
    
    code = models.CharField(max_length=8,verbose_name='Nome da role em inglês',choices=ROLES_CODE,default=ADMIN_CODE)
    name = models.CharField(verbose_name='Nome da role em portugês',choices=ROLES_NAME,default=ADMIN_NAME)

    def __str__(self):
        return self.name
    
    class Meta:
        app_label = 'role'
        db_table  = f'{app_label}'