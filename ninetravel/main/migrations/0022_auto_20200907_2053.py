# Generated by Django 3.0.8 on 2020-09-07 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_pricingrecord_price7days'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='price',
            name='site',
        ),
        migrations.AddField(
            model_name='pricingrecord',
            name='site',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='st', to='main.Site'),
            preserve_default=False,
        ),
    ]
