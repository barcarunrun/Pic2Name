# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-13 02:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileNameModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=50)),
                ('upload_time', models.DateTimeField(auto_now_add=True)),
                ('userID', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='myapp')),
                ('file_name', models.CharField(max_length=50)),
                ('upload_time', models.DateTimeField(auto_now_add=True)),
                ('userID', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result1', models.CharField(max_length=50)),
                ('result2', models.CharField(max_length=50)),
                ('result3', models.CharField(max_length=50)),
                ('result4', models.CharField(max_length=50)),
                ('result5', models.CharField(max_length=50)),
                ('result6', models.CharField(max_length=50)),
                ('result7', models.CharField(max_length=50)),
                ('result8', models.CharField(max_length=50)),
                ('result9', models.CharField(max_length=50)),
                ('result10', models.CharField(max_length=50)),
                ('score1', models.DecimalField(decimal_places=10, max_digits=11)),
                ('score2', models.DecimalField(decimal_places=10, max_digits=11)),
                ('score3', models.DecimalField(decimal_places=10, max_digits=11)),
                ('score4', models.DecimalField(decimal_places=10, max_digits=11)),
                ('score5', models.DecimalField(decimal_places=10, max_digits=11)),
                ('score6', models.DecimalField(decimal_places=10, max_digits=11)),
                ('score7', models.DecimalField(decimal_places=10, max_digits=11)),
                ('score8', models.DecimalField(decimal_places=10, max_digits=11)),
                ('score9', models.DecimalField(decimal_places=10, max_digits=11)),
                ('score10', models.DecimalField(decimal_places=10, max_digits=11)),
                ('result_from_user', models.CharField(max_length=50)),
                ('result_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
