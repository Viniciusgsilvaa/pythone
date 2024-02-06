from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, BaseUserManager


class UsuarioManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password, **extra__fields):
        if not email:
            raise ValueError('o e-mail é obrigadorio')
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra__fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, password=None, **extra__fields):
        extra__fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra__fields)

    def create_superuser(self, email, password=None, **extra__fields):
        extra__fields.setdefault('is_superuser', True)
        extra__fields.setdefault('is_staff', True)

        if extra__fields('is_superuser') is not True:
            raise ValueError('O Superuser precisa ter is_superuser=True')
        if extra__fields('is_staff') is not True:
            raise ValueError('O Superuser precisa ter is_staff=True')
        
        return self._create_user(email, password, **extra__fields)

class CustomUsuario(AbstractUser):
    email = models.EmailField('E-mail', unique=True)
    fone = models.CharField('Telefone', max_length=15)
    is_staff = models.BooleanField('Membro da equipe', default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'fone']

    def __str__(self):
        return self.email
    
    objects = UsuarioManager()

