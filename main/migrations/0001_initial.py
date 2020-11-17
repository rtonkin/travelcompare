# Generated by Django 3.0.8 on 2020-11-17 10:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('text', models.TextField(max_length=5000)),
                ('sort', models.IntegerField()),
                ('showonhomepage', models.BooleanField(default=False)),
                ('thumbnailfilename', models.CharField(max_length=100)),
                ('backgroundfilename', models.CharField(max_length=100)),
                ('shopdestination', models.BooleanField(default=False)),
                ('shopdestinationname', models.CharField(max_length=120)),
                ('shopproduct', models.BooleanField(default=False)),
                ('shopproductname', models.CharField(max_length=120)),
                ('seokeywords', models.CharField(max_length=200)),
                ('seodescription', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=60)),
                ('content', models.TextField(max_length=3000)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=32)),
                ('owner', models.CharField(blank=True, max_length=32, null=True)),
                ('displayURL', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=150)),
                ('established', models.CharField(max_length=4)),
                ('languages', models.IntegerField()),
                ('sitelink', models.CharField(max_length=80)),
                ('applink', models.CharField(blank=True, max_length=80, null=True)),
                ('logofilename', models.CharField(max_length=50)),
                ('bgimagefilename', models.CharField(max_length=50)),
                ('attprice', models.IntegerField(default=50)),
                ('attcoverage', models.IntegerField(default=50)),
                ('atteaseofuse', models.IntegerField(default=50)),
                ('attreputation', models.IntegerField(default=50)),
                ('prodhotels', models.BooleanField(default=False)),
                ('prodflights', models.BooleanField(default=False)),
                ('prodcarrentals', models.BooleanField(default=False)),
                ('prodtrains', models.BooleanField(default=False)),
                ('prodcruises', models.BooleanField(default=False)),
                ('prodtransfers', models.BooleanField(default=False)),
                ('prodtickets', models.BooleanField(default=False)),
                ('prodtours', models.BooleanField(default=False)),
                ('genericlinkhotels', models.CharField(max_length=500)),
                ('genericlinkflights', models.CharField(max_length=500)),
                ('genericlinkcarrentals', models.CharField(max_length=500)),
                ('genericlinktrains', models.CharField(max_length=500)),
                ('genericlinkcruises', models.CharField(max_length=500)),
                ('genericlinktransfers', models.CharField(max_length=500)),
                ('genericlinktickets', models.CharField(max_length=500)),
                ('genericlinktours', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='SiteProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descoverviewcontent', models.CharField(default='', max_length=2000)),
                ('descfeaturescontent', models.CharField(default='', max_length=2000)),
                ('descpricingcontent', models.CharField(default='', max_length=2000)),
                ('descavailabilitycontent', models.CharField(default='', max_length=2000)),
                ('descaccessibilitycontent', models.CharField(default='', max_length=2000)),
                ('descpaymentcontent', models.CharField(default='', max_length=2000)),
                ('descreputationcontent', models.CharField(default='', max_length=2000)),
                ('descservicecontent', models.CharField(default='', max_length=2000)),
                ('descsummarycontent', models.CharField(default='', max_length=2000)),
                ('descsdealscontent', models.CharField(default='', max_length=2000)),
                ('switchdeals', models.BooleanField(default=False)),
                ('paymentvisa', models.BooleanField(default=False)),
                ('paymentmastercard', models.BooleanField(default=False)),
                ('paymentamex', models.BooleanField(default=False)),
                ('paymentpaypal', models.BooleanField(default=False)),
                ('paymentapplepay', models.BooleanField(default=False)),
                ('paymentgooglepay', models.BooleanField(default=False)),
                ('sppriceraw', models.FloatField(default=0)),
                ('spprice', models.IntegerField(default=50)),
                ('spcoverage', models.IntegerField(default=50)),
                ('speaseofuse', models.IntegerField(default=50)),
                ('spreputation', models.IntegerField(default=50)),
                ('link', models.CharField(max_length=200)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='main.Product')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sites', to='main.Site')),
            ],
        ),
        migrations.CreateModel(
            name='PricingRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=100)),
                ('price7days', models.FloatField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prods', to='main.Product')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='st', to='main.SiteProduct')),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('daterecorded', models.DateField(default=datetime.date.today)),
                ('pricingrecord', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pr', to='main.PricingRecord')),
            ],
            options={
                'unique_together': {('pricingrecord', 'daterecorded')},
            },
        ),
    ]
