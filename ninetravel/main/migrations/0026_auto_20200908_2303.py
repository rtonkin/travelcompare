# Generated by Django 3.0.8 on 2020-09-08 13:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_auto_20200908_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='daterecorded',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterUniqueTogether(
            name='price',
            unique_together={('pricingrecord', 'daterecorded')},
        ),
    ]
