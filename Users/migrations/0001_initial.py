# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-30 17:22
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BasicInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(2)])),
                ('sex', models.BooleanField(default=False)),
                ('createDate', models.DateTimeField()),
                ('updateDate', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
