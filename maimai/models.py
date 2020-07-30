from django.db import models
from django.contrib.auth.models import AbstractUser
import django.core.validators
# Create your models here.

class CustomUser(AbstractUser):
    # is_customer = models.BooleanField(default=False)
    # is_seller = models.BooleanField(default=False)
    pass

    def __str__(self):
        return self.username

class Customer(models.Model):
    GENDER_CHOICES = (
        ('M','Male'),
        ('F','Female'),
    )
    username = models.CharField(error_messages={'unique': 'A user with that username already exists.'},
                                verbose_name='Username', max_length=20,
                                #help_text='20 characters or fewer. Letters, digits and @/./+/-/_ characters only.',
                                unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$',
                                                                                               'Enter a valid username. This may only contain letters, digits, and @/./+/-/_ characters.',
                                                                                               'invalid')])
    password = models.CharField(verbose_name='password', max_length=128)
    first_name = models.CharField(verbose_name='first Name',max_length=30)
    last_name = models.CharField(verbose_name='last Name',max_length=30)
    email = models.EmailField(verbose_name='email',max_length=254)
    gender = models.CharField(verbose_name='gender',max_length=1,choices=GENDER_CHOICES)
    birthday = models.DateField(verbose_name='Birthday',null=True,blank=True)

    def __str__(self):
        return self.username
