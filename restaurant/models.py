from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.conf import settings

class Customer(models.Model):
    CU_PK = models.AutoField(primary_key=True)
    CU_User = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    CU_Username = models.CharField(max_length=15, verbose_name='Username')
    CU_First_name = models.CharField(max_length=25, verbose_name='First Name')
    CU_Last_name = models.CharField(max_length=25, verbose_name='Last Name')
    CU_Email = models.CharField(max_length=45, verbose_name='Email Address')
    CU_Phone = models.CharField(max_length=15, verbose_name='Phone')
    CU_Address = models.CharField(max_length=45, verbose_name='Address')

def create_customer_profile(sender, **kwargs):
    if kwargs['created']:
        customer_profile = Customer.objects.create(CU_User=kwargs['instance'])
        customer_profile.save()
post_save.connect(create_customer_profile, sender=User)


class Employee(models.Model):
    EM_PK = models.AutoField(primary_key=True)
    EM_User = models.OneToOneField(User, on_delete=models.CASCADE)
    EM_Username = models.CharField(max_length=15, verbose_name='Username')
    EM_First_name = models.CharField(max_length=25, verbose_name='First Name')
    EM_Last_name = models.CharField(max_length=25, verbose_name='Last Name')
    EM_Email = models.CharField(max_length=45, verbose_name='Email Address')
    EM_BR = models.ForeignKey('Branch', on_delete=models.SET_NULL, null=True, verbose_name='Branch')
    EM_EM_Manager = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True, verbose_name='Manager')

def create_employee_profile(sender, **kwargs):
    if kwargs['created']:
        employee_profile = Employee.objects.create(EM_User=kwargs['instance'])
        employee_profile.save()

post_save.connect(create_employee_profile, sender=User)

class Branch(models.Model):
    BR_PK = models.AutoField(primary_key=True)
    BR_Name = models.CharField(max_length=45, verbose_name='Name')
    BR_Address = models.CharField(max_length=45, verbose_name='Address')

class Category(models.Model):
    CA_PK = models.AutoField(primary_key=True)
    CA_Name = models.CharField(max_length=45, verbose_name='Name')

class Item(models.Model):
    IT_PK = models.AutoField(primary_key=True)
    IT_CA = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, verbose_name='Category')
    IT_Name = models.CharField(max_length=45, verbose_name='Name')
    IT_Price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')
    IT_Profit = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Profit')
    IT_Calories = models.IntegerField(verbose_name='Calories')
    IT_GluttenFree = models.BooleanField(verbose_name='Glutten Free')
    IT_Vegetarian = models.BooleanField(verbose_name='Vegetarian')
    IT_Image = models.ImageField(default='default.png', upload_to='menu_items', verbose_name='Image')

class BranchItem(models.Model):
    BI_PK = models.AutoField(primary_key=True)
    BI_IT = models.ForeignKey('Item', on_delete=models.CASCADE)
    BI_BR = models.ForeignKey('Branch', on_delete=models.CASCADE)
    BI_IsAvailable = models.BooleanField()

class Table(models.Model):
    TA_PK = models.AutoField(primary_key=True)
    TA_BR = models.ForeignKey('Branch', on_delete=models.CASCADE, verbose_name='Branch')
    TA_Code = models.CharField(max_length=10, verbose_name='Code')
    TA_Seats = models.IntegerField(verbose_name='Number of seats')

class Reservation(models.Model):
    RS_PK = models.AutoField(primary_key=True)
    RS_CU = models.ForeignKey('Customer', on_delete=models.CASCADE)
    RS_TA = models.ForeignKey('Table', on_delete=models.CASCADE)
    RS_People = models.IntegerField(verbose_name='Number of people')
    RS_Start = models.DateTimeField(verbose_name='Start time')
    RS_End = models.DateTimeField(verbose_name='End time')

class Receipt(models.Model):
    RC_PK = models.AutoField(primary_key=True)
    RC_OR = models.OneToOneField('Order', on_delete=models.SET_NULL, null=True)
    RC_CU = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True)
    RC_TotalPrice = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Total price')
    RC_TotalProfit = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Total profit')

class Order(models.Model):
    OR_PK = models.AutoField(primary_key=True)
    OR_BR = models.ForeignKey('Branch', on_delete=models.CASCADE)

class OrderItem(models.Model):
    OI_PK = models.AutoField(primary_key=True)
    OI_BI = models.ForeignKey('BranchItem', on_delete=models.SET_NULL, null=True)
    OI_OR = models.ForeignKey('Order', on_delete=models.SET_NULL, null=True)

