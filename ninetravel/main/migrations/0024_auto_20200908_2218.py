# Generated by Django 3.0.8 on 2020-09-08 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20200908_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricingrecord',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='st', to='main.SiteProduct'),
        ),
    ]
