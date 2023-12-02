from django.db import models
from .forms import CreateUserForm


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True,  default='example@email.com', help_text='required')
    password1 = models.CharField(max_length=20, default='yourpassword')
    password2 = models.CharField(max_length=20, default='confirmpassword')



    class Meta:
        db_table = "myproject"
