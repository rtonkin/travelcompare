# Generated by Django 3.0.8 on 2021-02-07 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_site_visible'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteproduct',
            name='descfeaturescontent',
            field=models.CharField(default='', max_length=5000),
        ),
    ]
