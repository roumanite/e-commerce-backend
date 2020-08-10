from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser,PermissionsMixin
import django.core.validators
from django import forms
from .validators import MinimumLengthValidator
# Create your models here.

class CustomUser(AbstractUser):
    # is_customer = models.BooleanField(default=False)
    # is_seller = models.BooleanField(default=False)
    # def create_user(self,username,password,confirm_password,first_name,last_name,email,gender,birthday):
    #     user = self.model(username=username,password=password,confirm_password=confirm_password,
    #                       first_name=first_name,last_name=last_name,email=email,gender=gender,birthday=birthday)
    #     user.is_superuser = False
    #     user.is_admin = False
    #     user.is_staff = False
    #     user.set_password(password)
    #     # user.set_password(confirm_password)
    #     user.save(using=self._db)
    #     return user
    #
    # def create_user(self, email, password=None, **extra_fields):
    #     extra_fields.setdefault('is_superuser', False)
    #     return self._create_user(email, password, **extra_fields)
    #
    # def create_superuser(self, email, password, **extra_fields):
    #     extra_fields.setdefault('is_superuser', True)
    #     if extra_fields.get('is_superuser') is not True:
    #         raise ValueError('Superuser must have is_superuser=True.')
    #
    #     return self._create_user(email, password, **extra_fields)
    #
    # def __str__(self):
    #     return self.username
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('first_name', 'last_name', 'email','gender', 'birthday')

    username = models.CharField(error_messages={'unique': 'A user with that username already exists.'},
                                verbose_name='Username', max_length=20,
                                # help_text='20 characters or fewer. Letters, digits and @/./+/-/_ characters only.',
                                unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$',
                                                                                               'Enter a valid username. This may only contain letters, digits, and @/./+/-/_ characters.',
                                                                                               'invalid')])
    # password = models.CharField(verbose_name='password', max_length=128)
    # confirm_password = models.CharField(verbose_name='confirm password', max_length=128)
    first_name = models.CharField(verbose_name='first Name', max_length=30)
    last_name = models.CharField(verbose_name='last Name', max_length=30)
    email = models.EmailField(verbose_name='email', max_length=254,unique=True)
    gender = models.CharField(verbose_name='gender', max_length=1, choices=GENDER_CHOICES,default='')
    birthday = models.DateField(verbose_name='Birthday', null=True, blank=True)

    def __str__(self):
        return self.username

class Address(models.Model):
    full_name = models.CharField("Full Name",max_length=50)
    phone_number = models.CharField("Phone Number",max_length=15,blank=True,null=True)
    postal_code = models.CharField("Postal Code",max_length=12)
    unit_number = models.CharField("Unit Number",max_length=10)
    house_number = models.CharField("House Number",max_length=10)
    building = models.CharField("Building",max_length=30)
    street_name = models.CharField("Street Name",max_length=30)

    class Meta:
        abstract = False
        verbose_name = "Shipping Address"

# class Customer(models.Model):
#     GENDER_CHOICES = (
#         ('M','Male'),
#         ('F','Female'),
#     )
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ('username','password,','first_name','last_name','email','gender','birthday')
#
#     username = models.CharField(error_messages={'unique': 'A user with that username already exists.'},
#                                 verbose_name='Username', max_length=20,
#                                 #help_text='20 characters or fewer. Letters, digits and @/./+/-/_ characters only.',
#                                 unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$',
#                                                                                                'Enter a valid username. This may only contain letters, digits, and @/./+/-/_ characters.',
#                                                                                                'invalid')])
#     password = models.CharField(verbose_name='password', max_length=128)
#     first_name = models.CharField(verbose_name='first Name',max_length=30)
#     last_name = models.CharField(verbose_name='last Name',max_length=30)
#     email = models.EmailField(verbose_name='email',max_length=254)
#     gender = models.CharField(verbose_name='gender',max_length=1,choices=GENDER_CHOICES)
#     birthday = models.DateField(verbose_name='Birthday',null=True,blank=True)
#
#     def __str__(self):
#         return self.username
