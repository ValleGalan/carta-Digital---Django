from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    #entrar en admin con el correo
    email = models.EmailField(unique=True)
    USERNAME_FIELD ='email'
    REQUIRED_FIELDS = []
    pass