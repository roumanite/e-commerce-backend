from djmoney.models.fields import MoneyField
from django.db import models
from django_mysql.models import JSONField, Model
from mptt.models import MPTTModel, TreeForeignKey

class Category(MPTTModel):
  name = models.CharField(max_length=50)
  parent = TreeForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

class Listing(models.Model):
  id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  new_condition = models.BooleanField()
  category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)

class Stock_Keeping_Unit:
  id = models.AutoField(primary_key=True)
  price = MoneyField(default=0, default_currency='SGD')
  stock = models.PositiveIntegerField()
  variant = JSONField()