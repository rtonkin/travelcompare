# Generated by Django 3.0.8 on 2020-08-25 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_article_thumbnailfilename'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='showonhomepage',
            field=models.BooleanField(default=False),
        ),
    ]
