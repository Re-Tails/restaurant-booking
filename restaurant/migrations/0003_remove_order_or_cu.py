# Generated by Django 3.0.5 on 2020-05-29 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_auto_20200529_2119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='OR_CU',
        ),
    ]
