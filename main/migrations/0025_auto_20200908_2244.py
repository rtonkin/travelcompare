# Generated by Django 3.0.8 on 2020-09-08 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_auto_20200908_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteproduct',
            name='sppriceraw',
            field=models.FloatField(default=0),
        ),
    ]
