# Generated by Django 3.0.5 on 2020-05-30 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='OI_IT',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='restaurant.Item'),
            preserve_default=False,
        ),
    ]