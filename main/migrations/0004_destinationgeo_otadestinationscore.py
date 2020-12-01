# Generated by Django 3.0.8 on 2020-12-01 12:22

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20201124_2222'),
    ]

    operations = [
        migrations.CreateModel(
            name='DestinationGeo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('type', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='OtaDestinationScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('range', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='geos', to='main.DestinationGeo')),
                ('ota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='otas', to='main.Site')),
            ],
        ),
    ]
