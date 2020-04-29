# Generated by Django 3.0.4 on 2020-04-27 07:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('BR_PK', models.AutoField(primary_key=True, serialize=False)),
                ('BR_Name', models.CharField(max_length=45)),
                ('BR_Address', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='BranchItem',
            fields=[
                ('BI_PK', models.AutoField(primary_key=True, serialize=False)),
                ('BI_IsAvailable', models.BooleanField()),
                ('BI_BR', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.Branch')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('CA_PK', models.AutoField(primary_key=True, serialize=False)),
                ('CA_Name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('CU_PK', models.AutoField(primary_key=True, serialize=False)),
                ('CU_Phone', models.CharField(max_length=15)),
                ('CU_Address', models.CharField(max_length=45)),
                ('CU_User', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('OR_PK', models.AutoField(primary_key=True, serialize=False)),
                ('OR_BR', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.Branch')),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('TA_PK', models.AutoField(primary_key=True, serialize=False)),
                ('TA_Code', models.CharField(max_length=10)),
                ('TA_Seats', models.IntegerField()),
                ('TA_BR', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.Branch')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('RS_PK', models.AutoField(primary_key=True, serialize=False)),
                ('RS_People', models.IntegerField()),
                ('RS_Start', models.DateTimeField()),
                ('RS_End', models.DateTimeField()),
                ('RS_CU', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.Customer')),
                ('RS_TA', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.Table')),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('RC_PK', models.AutoField(primary_key=True, serialize=False)),
                ('RC_TotalPrice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('RC_TotalProfit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('RC_CU', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='restaurant.Customer')),
                ('RC_OR', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='restaurant.Order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('OI_PK', models.AutoField(primary_key=True, serialize=False)),
                ('OI_BI', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='restaurant.BranchItem')),
                ('OI_OR', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='restaurant.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('IT_PK', models.AutoField(primary_key=True, serialize=False)),
                ('IT_Name', models.CharField(max_length=45)),
                ('IT_Price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('IT_Profit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('IT_Calories', models.IntegerField()),
                ('IT_GluttenFree', models.BooleanField()),
                ('IT_Vegetarian', models.BooleanField()),
                ('IT_Image', models.ImageField(default='default.png', upload_to='menu_items')),
                ('IT_CA', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='restaurant.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('EM_PK', models.AutoField(primary_key=True, serialize=False)),
                ('EM_BR', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='restaurant.Branch')),
                ('EM_EM_Manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='restaurant.Employee')),
                ('EM_User', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='branchitem',
            name='BI_IT',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.Item'),
        ),
    ]