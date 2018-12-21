# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-19 09:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField(max_length=5000)),
                ('updated', models.DateField(auto_now=True)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]