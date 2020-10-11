from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db.models.expressions import Value

from items.models import Item
# Create your models here.
class UserManager(BaseUserManager):
    use_in_migrations = True
    
    def create_user(self, username, name, password=None):
        if not username:
            raise ValueError(_('Insert Your Username'))
        user = self.model(username=username, name=name)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, name):
        user = self.create_user(
            username=username,
            name=name,
            password=password
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    username = models.EmailField(unique=True)
    name = models.CharField(max_length=20)
    likes = models.ManyToManyField(to=Item, related_name='likers')
    subscribes = models.ManyToManyField(to=Item, related_name='subscribers')
    
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    
    object = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name']

    class Meta:
        def __str__(self):
            return self.username

