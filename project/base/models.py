from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.
class BaseModel(models.Model, User):
    uuid=models.UUIDField(primary_key=True, editable=False, default=uuid.uuid1)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    is_active=User.is_active

    class Meta:
        abstract=True