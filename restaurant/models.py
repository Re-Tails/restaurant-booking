from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

#class UserProfile(models.Model):
   # user = models.OneToOneField(User, on_delete=models.CASCADE)
    #description = models.CharField(max_length=100, default='')
    #address = models.CharField(max_length=100, default='')
    #phone = models.IntegerField(default=0)

#def create_profile(sender, **kwargs):
    #if kwargs['created']:
       # user_profile = UserProfile.objects.create(user=kwargs['instance'])

#post_save.connect(create_profile, sender=User)


class Customer(models.Model):
    CU_PK = models.AutoField(primary_key=True)
    CU_User = models.OneToOneField(User, on_delete=models.CASCADE)
    #username, first_name, last_name, email, password
    CU_Phone = models.CharField(max_length=15)
    CU_Address = models.CharField(max_length=45)

def create_customer_profile(sender, **kwargs):
    if kwargs['created']:
        customer_profile = Customer.objects.create(user=kwargs['instance'])

post_save.connect(create_customer_profile, sender=User)

class Employee(models.Model):
    EM_PK = models.AutoField(primary_key=True)
    EM_User = models.OneToOneField(User, on_delete=models.CASCADE)
    #username, first_name, last_name, email, password
    EM_BR = models.ForeignKey('Branch', on_delete=models.SET_NULL, null=True)
    EM_EM_Manager = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True)

def create_employee_profile(sender, **kwargs):
    if kwargs['created']:
        employee_profile = Employee.objects.create(user=kwargs['instance'])

post_save.connect(create_employee_profile, sender=User)

class Branch(models.Model):
    BR_PK = models.AutoField(primary_key=True)
    BR_Name = models.CharField(max_length=45)
    BR_Address = models.CharField(max_length=45)

class Category(models.Model):
    CA_PK = models.AutoField(primary_key=True)
    CA_Name = models.CharField(max_length=45)

class Item(models.Model):
    IT_PK = models.AutoField(primary_key=True)
    IT_CA = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    IT_Name = models.CharField(max_length=45)
    IT_Price = models.DecimalField(max_digits=10, decimal_places=2)
    IT_Profit = models.DecimalField(max_digits=10, decimal_places=2)
    IT_Calories = models.IntegerField()
    IT_GluttenFree = models.BooleanField()
    IT_Calories = models.BooleanField()
    IT_Image = models.ImageField(default='default.png', upload_to='menu_items')

class BranchItem(models.Model):
    BI_PK = models.AutoField(primary_key=True)
    BI_IT = models.ForeignKey('Item', on_delete=models.CASCADE)
    BI_BR = models.ForeignKey('Branch', on_delete=models.CASCADE)
    BI_IsAvailable = models.BooleanField()

class Table(models.Model):
    TA_PK = models.AutoField(primary_key=True)
    TA_BR = models.ForeignKey('Branch', on_delete=models.CASCADE)
    TA_Code = models.CharField(max_length=10)
    TA_Seats = models.IntegerField()

class Reservation(models.Model):
    RS_PK = models.AutoField(primary_key=True)
    RS_CU = models.ForeignKey('Customer', on_delete=models.CASCADE)
    RS_TA = models.ForeignKey('Table', on_delete=models.CASCADE)
    RS_People = models.IntegerField()
    RS_Start = models.DateTimeField()
    RS_End = models.DateTimeField()

class Receipt(models.Model):
    RC_PK = models.AutoField(primary_key=True)
    RC_OR = models.OneToOneField('Order', on_delete=models.SET_NULL, null=True)
    RC_CU = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True)
    RC_TotalPrice = models.DecimalField(max_digits=10, decimal_places=2)
    RC_TotalProfit = models.DecimalField(max_digits=10, decimal_places=2)

class Order(models.Model):
    OR_PK = models.AutoField(primary_key=True)
    OR_BR = models.ForeignKey('Branch', on_delete=models.CASCADE)

class OrderItem(models.Model):
    OI_PK = models.AutoField(primary_key=True)
    OI_BI = models.ForeignKey('BranchItem', on_delete=models.SET_NULL, null=True)
    OI_OR = models.ForeignKey('Order', on_delete=models.SET_NULL, null=True)

