# Generated by Django 3.0.8 on 2020-09-03 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_article_backgroundfilename'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='shopdestination',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='article',
            name='shopdestinationname',
            field=models.CharField(default='', max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='shopproduct',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='article',
            name='shopproductname',
            field=models.CharField(default='', max_length=120),
            preserve_default=False,
        ),
    ]
