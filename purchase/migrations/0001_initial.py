# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-04 15:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stocks', '0007_auto_20161004_0023'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchased',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Purchase_ID', models.CharField(max_length=100, null=True)),
                ('Purchase_Date', models.CharField(max_length=100, null=True)),
                ('Remarks', models.CharField(max_length=200, null=True)),
                ('ItemCode', models.CharField(max_length=100, null=True)),
                ('Base_Price', models.DecimalField(decimal_places=3, max_digits=8, null=True)),
                ('ProductName', models.CharField(max_length=100, null=True)),
                ('Capacity', models.CharField(max_length=100, null=True)),
                ('Old_Quantity', models.IntegerField(null=True)),
                ('Quantity', models.IntegerField(null=True)),
                ('Total_Quantity', models.IntegerField(null=True)),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stocks.Stock')),
            ],
        ),
    ]
