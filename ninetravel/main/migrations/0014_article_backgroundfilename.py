# Generated by Django 3.0.8 on 2020-09-03 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_feature'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='backgroundfilename',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
