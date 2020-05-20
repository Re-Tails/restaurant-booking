# Generated by Django 3.0.5 on 2020-05-09 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='BR_Address',
            field=models.CharField(max_length=45, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='branch',
            name='BR_Name',
            field=models.CharField(max_length=45, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='category',
            name='CA_Name',
            field=models.CharField(max_length=45, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='CU_Address',
            field=models.CharField(max_length=45, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='CU_Phone',
            field=models.CharField(max_length=15, verbose_name='Phone'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='EM_BR',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='restaurant.Branch', verbose_name='Branch'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='EM_EM_Manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='restaurant.Employee', verbose_name='Manager'),
        ),
        migrations.AlterField(
            model_name='item',
            name='IT_CA',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='restaurant.Category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='item',
            name='IT_Calories',
            field=models.IntegerField(verbose_name='Calories'),
        ),
        migrations.AlterField(
            model_name='item',
            name='IT_GluttenFree',
            field=models.BooleanField(verbose_name='Glutten Free'),
        ),
        migrations.AlterField(
            model_name='item',
            name='IT_Image',
            field=models.ImageField(default='default.png', upload_to='menu_items', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='item',
            name='IT_Name',
            field=models.CharField(max_length=45, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='item',
            name='IT_Price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='item',
            name='IT_Profit',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Profit'),
        ),
        migrations.AlterField(
            model_name='item',
            name='IT_Vegetarian',
            field=models.BooleanField(verbose_name='Vegetarian'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='RC_TotalPrice',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total price'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='RC_TotalProfit',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total profit'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='RS_End',
            field=models.DateTimeField(verbose_name='End time'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='RS_People',
            field=models.IntegerField(verbose_name='Number of people'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='RS_Start',
            field=models.DateTimeField(verbose_name='Start time'),
        ),
        migrations.AlterField(
            model_name='table',
            name='TA_BR',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.Branch', verbose_name='Branch'),
        ),
        migrations.AlterField(
            model_name='table',
            name='TA_Code',
            field=models.CharField(max_length=10, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='table',
            name='TA_Seats',
            field=models.IntegerField(verbose_name='Number of seats'),
        ),
    ]
