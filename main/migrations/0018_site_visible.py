# Generated by Django 3.0.8 on 2021-02-07 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20210207_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='visible',
            field=models.BooleanField(default=True),
        ),
    ]