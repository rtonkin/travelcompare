# Generated by Django 3.0.8 on 2021-01-02 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_qanda'),
    ]

    operations = [
        migrations.CreateModel(
            name='qAndATag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.AddField(
            model_name='qanda',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='main.qAndATag'),
        ),
    ]